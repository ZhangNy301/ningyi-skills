# LaTeX Snippets for Academic Papers

Common LaTeX code snippets for ML/NLP paper writing.

## Math Notation

### Basic Symbols

```latex
% Scalars (lowercase)
a, b, c, \ell (instead of l)

% Vectors (bold lowercase)
\mathbf{x}, \mathbf{h}, \boldsymbol{\alpha}

% Matrices (bold uppercase)
\mathbf{W}, \mathbf{X}, \boldsymbol{\Sigma}

% Sets (caligraphic)
\mathcal{D}, \mathcal{V}, \mathcal{E}

% Number fields
\mathbb{R}, \mathbb{N}, \mathbb{E}, \mathbb{P}
```

### Common Functions

```latex
\arg\max_{\theta} f(x)  % argmax
\max_{x} f(x)            % max
\min_{x} f(x)            % min
\exp(x)                  % exponential
\log(x)                  % logarithm
\sin(x), \cos(x), \tanh(x)  % trig functions
\det(\mathbf{A})         % determinant
\text{softmax}(\mathbf{x})  % multi-letter function
```

### Equations

```latex
% Single equation
\begin{equation}
    E = mc^2
\end{equation}

% Unnumbered equation
\begin{equation*}
    E = mc^2
\end{equation*}

% Aligned equations
\begin{align}
    y &= ax + b \\
    z &= cx + d
\end{align}

% Unnumbered aligned
\begin{align*}
    y &= ax + b \\
    z &= cx + d
\end{align*}

% Multi-line with cases
\begin{equation}
    f(x) = \begin{cases}
        1 & \text{if } x > 0 \\
        0 & \text{otherwise}
    \end{cases}
\end{equation}

% Auto-sized parentheses
\left( \sum_{i=1}^{n} x_i \right)
\left[ \int_{0}^{1} f(x) dx \right]
\left\{ x \middle| x \in \mathcal{X} \right\}
```

## Tables

### Basic Booktabs Table

```latex
\begin{table}[t]
\centering
\begin{tabular}{lcc}
\toprule
Model & Accuracy & F1 \\
\midrule
Baseline & 0.75 & 0.72 \\
Our Model & 0.82 & 0.80 \\
\bottomrule
\end{tabular}
\caption{Main results on the test set.}
\label{tab:main-results}
\end{table}
```

### Multi-column Header

```latex
\begin{table}[t]
\centering
\begin{tabular}{lcccc}
\toprule
& \multicolumn{2}{c}{Dev} & \multicolumn{2}{c}{Test} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5}
Model & Acc & F1 & Acc & F1 \\
\midrule
... & ... & ... & ... & ... \\
\bottomrule
\end{tabular}
\caption{Results on dev and test sets.}
\label{tab:dev-test}
\end{table}
```

### Resized Table

```latex
\begin{table}[t]
\centering
\small  % or \scriptsize, \footnotesize
\setlength{\tabcolsep}{4pt}  % Adjust column spacing
\begin{tabular}{...}
...
\end{tabular}
\caption{Caption text.}
\label{tab:my-label}
\end{table}
```

### Multi-row Cells

```latex
\usepackage{multirow}

\begin{table}[t]
\centering
\begin{tabular}{llcc}
\toprule
Type & Model & Acc & F1 \\
\midrule
\multirow{2}{*}{Baseline} & Model A & 0.75 & 0.72 \\
                        & Model B & 0.76 & 0.73 \\
\midrule
\multirow{2}{*}{Ours}   & Model C & 0.82 & 0.80 \\
                        & Model D & 0.83 & 0.81 \\
\bottomrule
\end{tabular}
\caption{Results with multi-row headers.}
\label{tab:multirow}
\end{table}
```

## Figures

### Single Figure

```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.8\linewidth]{figure.pdf}
\caption{Description of the figure.}
\label{fig:my-figure}
\end{figure}
```

### Subfigures

```latex
\usepackage{subcaption}

\begin{figure}[t]
\centering
\begin{subfigure}[b]{0.48\linewidth}
    \centering
    \includegraphics[width=\linewidth]{fig1a.pdf}
    \caption{Subfigure A.}
    \label{fig:sub-a}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.48\linewidth}
    \centering
    \includegraphics[width=\linewidth]{fig1b.pdf}
    \caption{Subfigure B.}
    \label{fig:sub-b}
\end{subfigure}
\caption{Overall caption. (a) shows X. (b) shows Y.}
\label{fig:main}
\end{figure}

% Reference: Figure~\ref{fig:main}(a)
```

## Citations

### Basic Citations

```latex
% Parenthetical (ACL/EMNLP/NAACL style)
Our model outperforms previous work \cite{smith2020}.
% Result: Our model outperforms previous work (Smith et al., 2020).

% In-text (ACL/EMNLP/NAACL style)
\citet{smith2020} proposed a new method.
% Result: Smith et al. (2020) proposed a new method.

% Multiple citations
\cite{smith2020,jones2021,lee2022}
```

### Citation with Pages

```latex
\citep[see][page 42]{smith2020}
% Result: (see Smith et al., 2020, page 42)
```

## Cross-References

```latex
\section{Method}
\label{sec:method}

\subsection{Architecture}
\label{sec:architecture}

As described in Section~\ref{sec:method}, ...
We detail the architecture in Section~\ref{sec:architecture}.

Figure~\ref{fig:results} shows ...
Table~\ref{tab:main-results} presents ...
Equation~\eqref{eq:emc2} defines ...
```

## Algorithms

```latex
\usepackage{algorithm}
\usepackage{algorithmic}

\begin{algorithm}[t]
\caption{My Algorithm}
\label{alg:my-alg}
\begin{algorithmic}[1]
\REQUIRE Input data $\mathcal{D}$, model parameters $\theta$
\ENSURE Trained model
\FOR{$i = 1$ to $N$}
    \STATE Compute loss $\mathcal{L}_i$
    \STATE Update $\theta \leftarrow \theta - \eta \nabla \mathcal{L}_i$
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

## Lists

### Bullet Points

```latex
\begin{itemize}
    \item First point
    \item Second point
    \item Third point
\end{itemize}
```

### Numbered List

```latex
\begin{enumerate}
    \item First step
    \item Second step
    \item Third step
\end{enumerate}
```

### Inline Bullets (Compact)

```latex
\noindent$\bullet$ Point 1

$\bullet$ Point 2

$\bullet$ Point 3
```

## URLs and Links

```latex
\usepackage{hyperref}

% URL
\url{https://github.com/example/repo}

% Clickable link
\href{https://example.com}{Link text}

% Email
\href{mailto:email@example.com}{email@example.com}
```

## Special Characters

```latex
% Non-breaking space
Figure~\ref{fig:1}  % Use ~ instead of space

% Em-dash
Text---more text

% En-dash
Pages 1--10

% Ellipsis
Text \ldots{} more text

% Degree
45$^\circ$

% Percent (in text)
50\%

% Ampersand (in text)
A \& B
```

## Common Packages

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{cleveref}  % Smart cross-references
\usepackage{multirow}
\usepackage{subcaption}
\usepackage{xcolor}
\usepackage{algorithm,algorithmic}
\usepackage{babel}  % Hyphenation patterns
```

## Comments and Notes

```latex
% Simple comment
\usepackage{todonotes}

% Inline todo
\todo{Add more experiments}

% Margin note
\todo[inline]{Important: Check this}

% Highlight for review
\textcolor{red}{TODO: Revise this paragraph}
```
