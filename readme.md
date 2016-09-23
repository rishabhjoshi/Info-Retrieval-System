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

## USAGE

### Index creation

Copy relevant documents in the corpus folder and call :

```python
python index_corpus.py -f
```

This will forced create the index of the docs present in corpus folder.

### Query

Run the boolean_query script and give your query in proper format as 
argument.

##### Eg 1

```python
python boolean_query.py '( eavril | ( avril & ( ! barron ) ) )'
```

A sample query is shown. Only queries in the 2 degree form are accepted.

The set of eavril consists of only e. Avril has a, c, b and barron has b.
The output has a c e.

##### Eg 2

```python
python boolean_query.py '( dont & ( ! eragon ) )'
```

The output for this document d.


## Contributions

I am yet to implement 
features so that a generic natural language boolean query can be processed.
Ill do it if time permits. Feel free to send in a pull req with enhancements, corrections.
The corresponding project files have the details about what all to do is left.

Give credits where they are due.

The corpus credits goes to S Gokula Krishnan.

Self-Motivated project by : RISHABH JOSHI - BITS Pilani
