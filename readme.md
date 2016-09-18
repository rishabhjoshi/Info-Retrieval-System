# Information Retrieval System

## Hierarchical Clustering of Research Papers

This self inspired project will cluster the research papers or any set of
documents in a hierarchical way, and display them in an interactive way
to ease the segregation process of the papers.

_May be used in parital fulfilment of the Course on IR_

### Project Details

**My Modules** : Folder containing self implemented algorithms. 

> _Use scikit learn if you want better implementation._

---

**Corpus** : Folder containing the corpus of documents

---

**Index** : Folder containing the index of all the terms (and their 
postings) in the document.

---

### Notes

* This implements a static indexer. You will need to index everything again
if you have a new file.

* Does not index numbers.

* Indexing is case insensitive and hyphenated words are treated as one.
( co-op is treated as coop)

* Todo - Implement porters algorithm for stemming

* Todo - extend from txt files to docs/odt and pdf

---

The corpus credits goes to github.com/gokul-uf/Boolean-Retrieval-System
