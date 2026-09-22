# A Classification of Mathieu's Second Conjecture for Reductive Spherical Pairs

## Abstract

Let $G$ be a connected complex reductive algebraic group and let $H\leq G$ be a reductive closed subgroup, not necessarily connected, such that $X=G/H$ is spherical. We prove that Mathieu's Second Conjecture holds for $(G,H)$ if and only if $G_{\mathrm{der}}\subseteq H$, equivalently if and only if the effective semisimple action on $X$ is trivial. The same condition characterizes when the kernel of the normalized Reynolds functional is a Mathieu--Zhao subspace.

When the condition fails, the proof gives fixed $P,Q\in\mathbb C[X]$ such that

$$
\mathfrak h_X(P^m)=0,
\qquad
\mathfrak h_X(QP^m)>0
\qquad(m\ge 1),
$$

and proves that $P$ lies outside the $G$-nullcone.

## Manuscript and source

- [Research draft PDF](mathieu_second_conjecture_spherical_pairs.pdf)
- [LaTeX source](mathieu_second_conjecture_spherical_pairs.tex)
- [Exact verification script](scripts/verify_calculations.py)
- [Checked verification output](scripts/verification_output.txt)

The manuscript is a research draft dated September 22, 2026. It has been model-assisted and audited internally, but is not yet independently peer reviewed or formally verified.

## Main classification

For reductive spherical pairs $(G,H)$ as above, the following are equivalent:

1. $(G,H)$ satisfies Mathieu's Second Conjecture;
2. $\ker \mathfrak h_X$ is a Mathieu--Zhao subspace of $\mathbb C[X]$;
3. $G_{\mathrm{der}}\subseteq H$;
4. the effective semisimple action on $G/H$ is trivial.

Equivalently,

$$
\text{Mathieu II holds for }(G,H)
\quad\Longleftrightarrow\quad
G_{\mathrm{der}}\subseteq \mathrm{core}_G(H).
$$

## Proof structure

The proof combines:

- a fixed-marker nullcone lemma based on affine Hilbert--Mumford;
- the universal radial identity from [The Mathieu Property for Compact Connected Lie Groups](https://github.com/long-mathematics/mathieu-property-compact-connected-lie-groups), arXiv:2609.16178;
- a root-doublet argument using classical $A_2$ and $B_2$ branching rules;
- an explicit Weyl-even moment circuit on $\mathrm{SL}_2/N(T)$;
- a subdirect-product argument for products of $\mathrm{SL}_2$ factors;
- Duistermaat--van der Kallen for the toral direction.

No spherical-localization transfer theorem or classification of spherical subgroups is assumed.

## Reproducible checks

The supplementary exact checks require Python 3.10+ and SymPy.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/check_verification.py
```

The script checks the $\mathrm{SL}_2/N(T)$ polynomial identity and 114 direct moment identities, together with 960 $A_2$ and 440 $B_2$ branching-selection/dimension checks. These finite checks are supplementary diagnostics, not substitutes for the general proofs.

Compile the manuscript with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error mathieu_second_conjecture_spherical_pairs.tex
```

## Related work

The principal companion result is:

- Christopher D. Long, [The Mathieu Property for Compact Connected Lie Groups](https://github.com/long-mathematics/mathieu-property-compact-connected-lie-groups), arXiv:2609.16178.

That paper classifies the compact-connected Mathieu property and supplies the radial-transfer theorem used here.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). The draft does not yet have an arXiv identifier or DOI.

## License

Code and repository infrastructure are provided under the [MIT License](LICENSE). The mathematical manuscript remains attributable to Christopher D. Long as stated in the paper.
