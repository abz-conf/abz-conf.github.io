---
title: "Validating Multiple Variants of an Automotive Light System with Electrum"

authors:
  - Alcino Cunha
  - Nuno Macedo
  - Chong Liu

date: 2020-06-03

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
  - 1 # conference paper

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
  - ABZ'20

categories: []

featured: false

projects:
  - abz20

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_26.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_26
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/cunha22020abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/cunha22020abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/cunha22020abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/cunha22020abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

This paper reports on the development and validation of a formal model for an automotive adaptive exterior lights system (ELS) with multiple variants in Electrum, a lightweight formal specification language that extends Alloy with mutable relations and temporal logic. We explore different strategies to address variability, one in pure Electrum and another through an annotative language extension. We then show how Electrum and its {\Analyzer} can be used to validate systems of this nature, namely by checking that the reference scenarios are admissible, and to automatically verify whether the established requirements hold. A prototype was developed to translate the provided validation sequences into Electrum and back to further automate the validation process. The resulting ELS model was validated against the provided validation sequences and verified for most of requirements for all variants.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_26.pdf" >}}

## Reference

```
% BibTex
@inproceedings{cunha22020abz,
  title={{Validating Multiple Variants of an Automotive Light System with Electrum}},
  author={Cunha, Alcino and Macedo, Nuno and Liu, Chong},
  booktitle={7th International Conference on Rigorous State Based Methods (ABZ'20)},
  pages={318--334},
  year={2020},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  Electrum
- **Resources and tools:**
  Electrum

  For more information, please contact the <a href ="mailto:nfmmacedo@di.uminho.pt">authors</a>
