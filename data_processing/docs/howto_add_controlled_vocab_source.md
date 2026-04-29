# How-to: add a new controlled vocabularies source and store it in a dedicated named graph

This document explains what to change in the codebase if you want to support **a new controlled vocabulary origin** (e.g. `https://datos.gob.es`) and store its vocabularies in a **new named graph**, for example:

- `http://data.dsb.com/graph/reference/source/datos-gob-es`

It covers both:

- **Automatic import at startup** (auto-import)
- **Manual import via API endpoint**

> Notes
> - Examples and code identifiers are based on the current repository structure.
> - Comments in code should remain in English.

---

## Quick checklist

- [ ] Add a new graph constant (environment + `crud.py`)
- [ ] Teach the auto-import bootstrap how to pick the new graph (new `source` value)
- [ ] Add a new folder under `resources/controlled_vocabularies/` for that source
- [ ] Ensure duplicate detection checks the correct graph
- [ ] (Optional) Extend the import endpoint to allow selecting the target graph/source

---

## 1) Add a new named graph constant

### 1.1 Add it to `.env`

Add a new env var:

- `DSB_GRAPH_VOCABS_DATOS_GOB_ES=http://data.dsb.com/graph/reference/source/datos-gob-es`

### 1.2 Expose it in `config/crud.py`

File: `src/dev/config/crud.py`

Add a new constant next to the existing ones:

- `DSB_GRAPH_VOCABS_OP_EU`
- `DSB_GRAPH_VOCABS_EXTENSIONS`

Example:

- `DSB_GRAPH_VOCABS_DATOS_GOB_ES = os.environ.get("DSB_GRAPH_VOCABS_DATOS_GOB_ES", "http://data.dsb.com/graph/reference/source/datos-gob-es")`

This ensures your deployment can override the graph without code changes.

---

## 2) Wire the new source into auto-import

Auto-import is orchestrated from:

File: `src/dev/services/controlled_vocabularies_bootstrap.py`

### 2.1 Add a new source graph constant

At the top of the file, where you currently have:

- `_CUSTOM_VOCABS_GRAPH_IRI = crud.DSB_GRAPH_VOCABS_EXTENSIONS`
- `_EU_VOCABS_GRAPH_IRI = crud.DSB_GRAPH_VOCABS_OP_EU`

Add:

- `_DATOS_GOB_ES_VOCABS_GRAPH_IRI = crud.DSB_GRAPH_VOCABS_DATOS_GOB_ES`

### 2.2 Add a new folder under `resources/controlled_vocabularies`

Create a directory for the new source, for instance:

- `src/dev/resources/controlled_vocabularies/datos_gob_es_vocabs/`

Then update `_iter_vocab_files(...)` to scan that folder. Today it scans:

- `custom_vocabs/*.xml`
- `eu_vocabs/*.{rdf,ttl,nt,jsonld,...}`

Add a third block:

- `datos_gob_es_vocabs/*.{rdf,ttl,nt,jsonld,xml}`

And yield `(file_path, "datos-gob-es")`.

### 2.3 Map the new source to its graph

Update `_target_graph_for_source(source: str) -> str` to support the new token:

- `"datos-gob-es" -> _DATOS_GOB_ES_VOCABS_GRAPH_IRI`

### 2.4 Update selection naming conventions (optional)

Currently `vocab_name` is `file_path.stem`.

If the same `vocab_name` could exist in multiple sources, you have two options:

1) Keep names unique across sources (simplest)
2) Prefix names by source in auto-import (e.g. `countries-datos-gob-es`)

If you choose (2), the change belongs in the bootstrap where `vocab_name` is derived.

---

## 3) Ensure duplicate detection checks the correct graph

Duplicate detection is implemented in:

File: `src/dev/repositories/controlled_vocabulary_repository.py`

Method:

- `find_duplicate_vocab(vocab_name: str, graph_iri: Optional[str] = None)`

Auto-import passes `graph_iri=target_graph_iri`, so **as long as your new source uses the correct target graph**, `skipped` will work.

Key points (how it works today):

- The repository tries to locate the ConceptScheme in the provided graph
- It uses internal metadata (`vocabName`) as the primary mechanism to match schemes whose IRI is not the internal one

If you add a new graph constant, no repository changes should be required unless:

- Your new source uses multiple ConceptSchemes per file
- The source doesn't expose a stable ConceptScheme, or you want a custom mapping

In those cases you would extend `_pick_scheme_in_graph(...)` and/or the importer.

---

## 4) Extend the import endpoint (manual import) to support the new graph

The import endpoint lives in:

File: `src/dev/apis/controlled_vocabularies/fastapi_controlled_vocabularies.py`

Today, the target graph is chosen via:

- `graph_base = repository.resolve_graph_base_for_import(is_xml_tabular=..., scheme_iri=...)`

And `resolve_graph_base_for_import(...)` (in the repository) decides between:

- OP-EU graph when `scheme_iri` starts with `http://publications.europa.eu`
- EXTENSIONS graph otherwise

### Option A (recommended): allow passing `source` or `graph_iri` explicitly

Add a new optional request parameter (either query param or form field):

- `source` (e.g. `custom`, `eu`, `datos-gob-es`)

or:

- `graph_iri` (absolute IRI)

Then implement:

- if the caller passes `graph_iri`, validate it and use it
- else if the caller passes `source`, map it to a graph constant
- else fallback to the current heuristic

Where to implement:

- `fastapi_controlled_vocabularies.py`: parse and validate request params
- `ControlledVocabularyRepository.resolve_graph_base_for_import(...)`: optionally accept `source` and override the heuristic

This avoids coupling to `scheme_iri` prefixes and scales cleanly to new sources.

### Option B: extend the heuristic

If you always know a prefix that identifies `datos.gob.es` vocabularies, extend:

- `ControlledVocabularyRepository.resolve_graph_base_for_import(...)`

Example logic:

- if `scheme_iri` starts with `https://datos.gob.es/` then target `DSB_GRAPH_VOCABS_DATOS_GOB_ES`

This is quick but becomes messy if multiple sources exist.

---

## 5) Add the resources for the new source

Depending on the source, you might ingest:

- RDF (RDF/XML, Turtle, N-Triples, JSON-LD)
- domain XML that must be parsed into RDF (like your tabular XML custom vocabs)

The conversion/parsing logic sits in:

File: `src/dev/services/controlled_vocabulary_importer.py`

If `datos.gob.es` provides RDF, it should be plug-and-play.

If it provides a custom XML/CSV format, you’ll need to add a parser similar to the existing XML tabular path.

---

## 6) Operational considerations

### 6.1 Graph naming

Keep graph IRIs:

- absolute
- stable
- environment-driven

### 6.2 Avoid name collisions

If two sources can have the same `vocab_name`, decide upfront how to disambiguate:

- prefix the vocab name
- or store same name in different graphs (works) but ensure APIs and UI always query the correct graph

### 6.3 Logging and troubleshooting

Auto-import logs live in:

- `src/dev/services/controlled_vocabularies_bootstrap.py`

You should see:

- started timestamp
- imported/skipped lists
- finished timestamp + elapsed time

---

## Summary: what you change for a new source

Minimum changes for a new source + new graph:

1) `.env` + `crud.py`: add `DSB_GRAPH_VOCABS_DATOS_GOB_ES`
2) `controlled_vocabularies_bootstrap.py`:
   - scan a new folder
   - yield a new `source` token
   - map `source` token to the new graph
3) Add resources folder and files

Optional changes:

- `fastapi_controlled_vocabularies.py`: allow selecting `source`/`graph_iri` explicitly
- `controlled_vocabulary_importer.py`: add parsing if the source isn’t RDF
