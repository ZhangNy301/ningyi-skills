# Detailed Paper Writing Guide

This document contains detailed examples and explanations from the Paper-Writing-Tips repository.

## Formula Notation Details

### 1. Scalar Notation

Use lowercase Latin letters for scalars. To avoid confusion between letter `l` and number `1`, use `\ell` instead.

```latex
% Bad
$l = 1$

% Good
$\ell = 1$
```

### 2. Structured Values

For structured values like sentence sequences, trees, or graphs, use `\boldsymbol`.

```latex
\boldsymbol{s} = (w_1, w_2, ..., w_n)
```

### 3. Sets of Structured Values

Use `\mathcal` for sets:

```latex
\mathcal{D} = \{\boldsymbol{s}_1, \boldsymbol{s}_2, ..., \boldsymbol{s}_n\}
```

### 4. Vectors and Matrices

```latex
% Vectors - lowercase bold
\mathbf{x}  % Latin letter
\boldsymbol{\alpha}  % Greek letter

% Matrices - uppercase bold
\mathbf{W}  % Latin letter
\boldsymbol{\Sigma}  % Greek letter
```

### 5. Number Fields and Operators

```latex
\mathbb{R}  % Real numbers
\mathbb{E}  % Expectation
\mathbb{P}  % Probability
```

### 6. Multi-letter Variable Names

Use `\textrm` or `\textit` for multi-letter identifiers:

```latex
% Bad
$softmax(x)$

% Good
$\textrm{softmax}(x)$
$\textit{proj}(x)$
$\textrm{enc}(x)$
```

### 7. Auto-sizing Parentheses

```latex
% Bad
$s = (\sum_{i=0}^{N-1}{\alpha_{i} h_i}) + h_N$

% Good
$\mathbf{s} = \left(\sum_{i=0}^{N-1}{\alpha_{i} \mathbf{h}_i}\right) + \mathbf{h}_N$

% Set notation with middle bar
$\left\{ x \middle| x \ne \frac{1}{2} \right\}$
```

### 8. Equation Alignment

```latex
% Bad - gather doesn't align
\begin{gather}
   E = m c^2 \\
   C = B \log_2\left(1+\frac{S}{N}\right)
\end{gather}

% Good - align at equals sign
\begin{align}
   E &= m c^2 \\
   C &= B \log_2\left(1+\frac{S}{N}\right)
\end{align}
```

### 9. Equation Numbering

```latex
% Only number referenced equations
\begin{equation}
   E = m c^2 \nonumber
\end{equation}
```

## Table Formatting

### Booktabs Style

```latex
\usepackage{booktabs}

\begin{table}[htbp]
   \centering
   \begin{tabular}{lcccccl}\toprule
      & \multicolumn{3}{c}{E} & \multicolumn{3}{c}{F}
      \\\cmidrule(lr){2-4}\cmidrule(lr){5-7}
               & $mv$  & Rel.~err & Time    & $mv$  & Rel.~err & Time\\\midrule
      A    & 11034 & 1.3e-7 & 3.9 & 15846 & 2.7e-11 & 5.6 \\
      B & 21952 & 1.3e-7 & 6.2 & 31516 & 2.7e-11 & 8.8 \\
      C & 15883 & 5.2e-8 & 7.1 & 32023 & 1.1e-11 & 1.4\\
      D  & 11180 & 8.0e-9 & 4.3 & 17348 & 1.5e-11 & 6.6
      \\\bottomrule
   \end{tabular}
   \caption{Results with booktabs.}
   \label{tab:results}
\end{table}
```

### Table Sizing

```latex
\small  % Reduce font size
\scriptsize  % Even smaller
\setlength{\tabcolsep}{8pt}  % Adjust column spacing
\centering  % Center the table
```

## Writing Style Guidelines

### Latin Abbreviations

| Abbreviation | Meaning | Example |
|-------------|---------|---------|
| e.g., | for example | We use NLP techniques, e.g., parsing and tagging. |
| i.e., | that is | We use the best model, i.e., BERT. |
| et al. | and others | Smith et al. proposed... |
| etc. | and others | tools, datasets, etc. |

**Note**: `et al.` and `etc.` don't need an extra period at the end of a sentence.

### Non-breaking Spaces

Use `~` before citations and references to prevent line breaks:

```latex
Figure~\ref{fig:results} shows the performance.
Table~\ref{tab:data} shows dataset details.
We use BERT~\cite{bert} as our encoder.
Section~\ref{sec:method} describes our method.
```

### English Quotation Marks

```latex
% Correct
``This is a quote.''

% Incorrect
"This is a quote."
"This is a quote."
```

## Citation Formats by Conference

### ACL/NAACL/EMNLP

```latex
% Parenthetical
\cite{smith2020}
% Result: (Smith et al., 2020)

% In-text
\citet{smith2020}
% Result: Smith et al. (2020)
```

### COLING

```latex
% In-text
\newcite{smith2020}
% Result: Smith et al. (2020)
```

### AAAI/IJCAI

```latex
% In-text
\citeauthor{smith2020} \shortcite{smith2020}
% Result: Smith et al. (2020)
```

### IEEE

```latex
% In-text
\citeauthor{smith2020}~(\citeyear{smith2020})
% Result: Smith et al. (2020)
```

## Common Mistakes to Avoid

### Word Choice

| Wrong | Right | Explanation |
|-------|-------|-------------|
| Firstly | First | Use First, Second, Third |
| testing set | test set | "test" is the noun |
| Bert, electra | BERT, ELECTRA | Keep official capitalization |
| obvious | straightforward | Avoid absolutes |
| always | generally/usually | Avoid absolutes |
| better (alone) | better at X because Y | Be specific |

### Articles

```latex
% Wrong - an before consonant sound
a LSTM

% Right - an before vowel sound
an LSTM
an F-score
an HMM
an N-gram

% a before consonant sound
a U-shape
a BERT model
```

### Tense

Use present tense for established facts and your paper's contributions:

```latex
% Good - present tense
We propose a new method.
The results show that our method outperforms baselines.

% Avoid - past tense for your contributions
We proposed a new method.
```

## Figure Design Guidelines

1. **Use vector graphics**: Save as PDF from matplotlib:
   ```python
   plt.savefig('figure.pdf', bbox_inches='tight')
   ```

2. **Font consistency**: Use the same font throughout the figure.

3. **Size**: Figure text should be readable but not larger than body text.

4. **Black-and-white friendly**: Don't rely solely on color. Use:
   - Different line styles (solid, dashed, dotted)
   - Different markers (circles, squares, triangles)
   - Different shades (dark vs light)

5. **Color palette**: Use no more than 6 colors. Avoid overly bright colors.

6. **Layout**: Keep arrows flowing in the same direction. Avoid isolated components.

## Pre-submission Checklist

### Content
- [ ] No author information (anonymous submission)
- [ ] No institution information in paper or code
- [ ] Title and abstract match submission system
- [ ] Page count within limits

### Formatting
- [ ] Consistent model name capitalization
- [ ] Consistent title capitalization style
- [ ] Proper citation format for venue
- [ ] Vector graphics for all figures
- [ ] Proper equation punctuation

### References
- [ ] No duplicate arXiv + published versions
- [ ] Consistent venue abbreviations
- [ ] Complete bib entries (year, pages, etc.)

### Code/Data
- [ ] No hardcoded paths
- [ ] No .git folder in submission
- [ ] README included

### Technical
- [ ] Grammar check with Grammarly/Writefull
- [ ] Backup with version number (e.g., v1_20240115)
- [ ] Submit early to avoid server issues

## Useful Tools

- **SimBiber**: Simplify bib entries with venue abbreviations
  - https://github.com/MLNLP-World/SimBiber

- **Rebiber**: Normalize bib entries from arXiv to published versions
  - https://github.com/yuchenlin/rebiber

- **ACL Pubcheck**: Check ACL paper submissions
  - https://github.com/acl-org/aclpubcheck

- **Grammarly**: Grammar and style checking
  - https://app.grammarly.com

- **Writefull**: Academic writing feedback
  - https://www.writefull.com
