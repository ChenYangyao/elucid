# ELUCID - Exploring the Local Universe with reConstructed Initial Density field

This repository contains usage for the data products of the ELUCID project. For a complete description of the method and the simulation, see [Huiyuan Wang et al. 2016](https://doi.org/10.3847/0004-637X/831/2/164) (ApJ 831, 164; Paper-III).

## About the project

### What we have done?

A method we developed for the reconstruction of the initial density field is applied to SDSS DR7 (North Cap, redshift $\approx 0 - 0.12$ ). A high-resolution N-body constrained simulation (CS; with $3072^3$ particles in a $500\ h^{-1}{\rm Mpc}$ box) is performed to evolve the reconstructed initial condition and recover the evolution history of the local Universe.
Statistical properties of cosmic web and halo populations are found to be accurately reproduced by the CS. 

### Example usages of the constrained simulation

***Robust quantification of the environments within which the observed galaxies reside***
- [Huiyuan Wang et al. 2018](https://doi.org/10.3847/1538-4357/aa9e01) (ApJ 852, 31; Paper-IV, galaxy quenching versus environment).

***Input fields, halos and merger trees for galaxy formation models*** (hydrodynamical, semi-analytical or empirical)
- [Xiaohu Yang et al. 2018](https://doi.org/10.3847/1538-4357/aac2ce) (ApJ 860, 30; Paper-V, neighborhood abundance matching); 
- [Renjie Li et al. 2022](https://doi.org/10.3847/1538-4357/ac8359) (ApJ 936, 11; Paper-VII, hydro for Coma, SDSS Great Wall, and a void);
- [Xiong Luo et al. 2024](https://doi.org/10.3847/1538-4357/ad392e) (ApJ 966, 236; Paper-VIII, hydro for Coma with variants for feedback models).

***Cosmic variance (CV)-free statistics of observed galaxies*** (even for a small sample)
- [Yangyao Chen et al. 2019](https://doi.org/10.3847/1538-4357/ab0208) (ApJ 872, 180; Paper-VI, CV-free galaxy luminosity and stellar mass functions);
- [Ziwen Zhang et al. 2025](https://doi.org/10.1038/s41586-025-08965-5) (Nature 642, 47--52; CV-free clustering measurements for SDSS dwarfs).

## Specification of the data products

### List of data products

- The density field at $z \approx 0$ recovered from SDSS DR7 (North Cap, $z \approx 0-0.12$) with the Halo-Domain method (hereafter Halo-Domain Field).
- The reconstructed initial density field at $z = z_{\rm ini}=100$ with an HMCMC method (hereafter Reconstructed Initial Field).
- The snapshots (dark-matter particles) of the constrained simulation (CS) at various redshifts (here after CS snapshots).
- The catalogs of FoF halos and Subfind subhalos identified from the CS snapshots (hereafter CS halo/subhalo catalogs).
- The SubLink subhalo merger trees that links subhalos across different snapshots (hereafter CS subhalo merger trees).

***Cosmology***: the project is performed in a flat $\Lambda$-CDM cosmology with parameters 
consistent with the WMAP5 results (Dunkley et al. 2009): 
$\Omega_{\rm K,0}=0$, $\Omega_{\rm M,0}=0.258$, $\Omega_{\rm B,0}=0.044$, 
$\Omega_{\rm \Lambda, 0}=0.742$, $H_0 = 100\ h\ {\rm km\ s^{-1}\ Mpc^{-1}}$ 
with $h=0.72$, and a spectral index of $n=0.96$ with an amplitude specified by 
$\sigma_8=0.80$ for the Gaussian initial density field.

***Configuration of the CS***:

|Property|value|explanation|
|---|---|---
| $N_{\rm snapshot}$ | 101 | Number of snapshots. Note that the last two snapshots are redundant -- just ignore the last one.|
| $N_{\rm chunks}$   | 2048   | Number of files into which each snapshot are stored |
| $L_{\rm box}$ | $500.0\ h^{-1}{\rm Mpc}$ | Side length of the periodic cubic box |
| $N_{\rm cell, all}$ | 16777216 | Number of space-filling (Peano-Hilbert) cells (i.e. $256^3$) used partition the simulation box |
| $N_{\rm p, all}$ | 28991029248 | Total number of dark matter particles (i.e. $3072^3$) in a snapshot |
| $m_{\rm p}$ | 0.03087502 | Mass (in $10^{10}\ h^{-1}\ M_\odot$) of each dark matter particle |
| $N_{\rm bit\ mask}$ | 36 | Number of bits used to store the particle IDs |
| $\epsilon_{\rm DM}$ | $3.5\ h^{-1}{\rm ckpc}$ | Gravitational softening length (comoving) |


***Available snapshots of the CS***:  A total of 100 snapshots, 
from redshift $z=18.4$ to $0$, are output.
Here we list the available snapshots ($s$) and the corresponding redshifts ($z$).

| s | z  | s  | z | s  | z  |s  | z  |s  | z  |
|---|---|---|---|---|---|---|---|---|---|
| 0   |  18.409561    |  20  |  9.661436    |  40    |  4.856104   |   60    |   2.216634    |   80    |    0.766834   |
| 1   |  17.837003    |  21  |  9.346719    |  41    |  4.683271   |   61    |   2.121703    |   81    |    0.714689   |
| 2   |  17.280867    |  22  |  9.041370    |  42    |  4.515537   |   62    |   2.029569    |   82    |    0.664085   |
| 3   |  16.741506    |  23  |  8.745069    |  43    |  4.352746   |   63    |   1.940156    |   83    |    0.614971   |
| 4   |  16.217927    |  24  |  8.457427    |  44    |  4.194778   |   64    |   1.853385    |   84    |    0.567310   |
| 5   |  15.709555    |  25  |  8.178270    |  45    |  4.041466   |   65    |   1.769170    |   85    |    0.521054   |
| 6   |  15.216655    |  26  |  7.907416    |  46    |  3.892679   |   66    |   1.687450    |   86    |    0.476161   |
| 7   |  14.737870    |  27  |  7.644537    |  47    |  3.748270   |   67    |   1.608133    |   87    |    0.432595   |
| 8   |  14.273472    |  28  |  7.389403    |  48    |  3.608146   |   68    |   1.531159    |   88    |    0.390316   |
| 9   |  13.822720    |  29  |  7.141798    |  49    |  3.472132   |   69    |   1.456453    |   89    |    0.349284   |
| 10   |  13.385178    |  30  |  6.901516    |  50    |  3.340146   |   70    |   1.383961    |   90    |    0.309461   |
| 11   |  12.960631    |  31  |  6.668300    |  51    |  3.212051   |   71    |   1.313599    |   91    |    0.270816   |
| 12   |  12.548667    |  32  |  6.442027    |  52    |  3.087756   |   72    |   1.245319    |   92    |    0.233310   |
| 13   |  12.148725    |  33  |  6.222355    |  53    |  2.967105   |   73    |   1.179053    |   93    |    0.196911   |
| 14   |  11.760799    |  34  |  6.009231    |  54    |  2.850019   |   74    |   1.114742    |   94    |    0.161586   |
| 15   |  11.384054    |  35  |  5.802351    |  55    |  2.736404   |   75    |   1.052330    |   95    |    0.127304   |
| 16   |  11.018653    |  36  |  5.601575    |  56    |  2.626131   |   76    |   0.991758    |   96    |    0.094034   |
| 17   |  10.663984    |  37  |  5.406766    |  57    |  2.519107   |   77    |   0.932976    |   97    |    0.061746   |
| 18   |  10.319644    |  38  |  5.217668    |  58    |  2.415254   |   78    |   0.875930    |   98    |    0.030411   |
| 19   |  9.985631    |  39  |  5.034165    |  59    |  2.314452   |   79    |   0.820565    |   99    |    0.000000   |

### The coordinate system

The Halo-Domain Field is reconstructed from SDSS. For the CS to be run from the field, 
the SDSS survey volume is embedded into a cubic box. Thus, all of data products are 
given in the simulation frame, unless specifically clarified.

The Cartesian coordinates in the observation frame (J2000; hereafter denoted with a subscript `J2000`) 
and in the simulation frame (hereafter denoted with a subscript `sim`) 
are related through a translation along $`\vec{x}_0`$ and a rotation in the $`x`$-$`y`$ plane:

$$\vec{x}_{\rm J2000} = \mathcal{R} (\vec{x}_{\rm sim} - \vec{x}_{\rm 0})\ ,$$

where the translation vector $\vec{x}_{\rm 0} = (370, 370, 30)\ h^{-1} {\rm Mpc}$,
the rotation matrix

$$
\mathcal{R} = \begin{pmatrix}
{\rm cos}(\phi_0)   &  {\rm sin}(\phi_0)    & 0 \\
{\rm cos}(\phi_0 + \frac{\pi}{2})   &   {\rm sin}(\phi_0 + \frac{\pi}{2})         &  0 \\
0  &  0   &   1
\end{pmatrix} ,
$$

and the rotation angle $\phi_0 = 39^{\circ}$.

The transformation is illustrated in the following figure:

[![frame-cvt.jpg](/docs/figures/frame-cvt-small.png)](/docs/figures/frame-cvt.png)

Note that
- The Cartesian coordinates in the `sim` frame is defined so that one corner of the cubic box is at the origin, 
and three sides of the box are along the Cartesian axes. This means all coordinates in the `sim` frame 
are in the range of $[0, 500]\ h^{-1}{\rm Mpc}$.
- The Cartesian coordinates in the `J2k` frame is defined so that the $+x$ axis 
points to `RA=0`, `Dec=0`, the $+y$ axis points to `RA=90 deg`, `Dec=0`, and the $+z$ axis 
points to `Dec=90 deg`. This means $`\vec{x}_{\rm J2000} = d_{\rm c} \left( \cos {\rm Dec} \cdot \cos {\rm RA}, \cos {\rm Dec} \cdot \sin {\rm RA}, \sin {\rm Dec} \right)`$
for a galaxy at comoving distance $d_{\rm c}$, right ascension `RA` and declination `Dec`.
- Rotation matrix ${\bf R}$ is orthogonal (i.e. ${\bf R}^{-1} = {\bf R}^{\rm T}$ can be used to transform from `J2000` back to `sim` coordinates).
- Vectors and tensors can also be transformed. For example, the velocity vector is transformed as $`\vec{v}_{\rm J2000} = \mathcal{R} \vec{v}_{\rm sim}`$.
