# no1s1

This repository contains resources and code for the no1s1 prototype and replaces the [old repo](https://github.com/Unawhatitis/no1s1_TI). It is managed by [Unawhatitis](https://github.com/Unawhatitis) and [hujens](https://github.com/hujens).

This prototype implementation started as a research effort between [Dezentrum](https://www.dezentrum.ch/en/) and [ETH Zurich Chair of IC](https://ic.ibi.ethz.ch/). We are now conducting research at the [ETH Zurich CEA lab](https://cea.ibi.ethz.ch/). The prototype is also exhibited or we give expert talks under the coordination of [no1s1 labs](https://www.no1s1labs.org/). If you are interested in collaboration, please reach out to us.

## The no1s1 Prototype

### Origin

The idea behind no1s1 to use blockchain, so things can own and organize themselves, was mentioned in several places. Noteworthy is especially the article on [Nature 2.0](https://blog.oceanprotocol.com/nature-2-0-27bdf8238071?gi=d17a83f090a1) by Trent McConaghy.

The no1s1 prototype was also not the first prototype of a self-owning thing. Primavera di Filippi built the [Plantoid](https://www.plantoid.org/), and an earlier prototype by Dezentrum was [SattelETH](https://www.dezentrum.ch/en/case-studies/ein-autonomer-satellit-auf-weltreise). But no1s1 was the first prototype that applied this idea to the built environment, the name and idea stemming from the think tank Dezentrum: [no1s1 Whitepaper](https://github.com/no1s1/whitepaper).

The subsequent collaboration between [Dezentrum](https://www.dezentrum.ch/en/) and [ETH Zurich Chair of IC](https://ic.ibi.ethz.ch/) lead then to the development of this prototype.

### Implementation

<figure><img src="media/no1s1.png" alt="Trulli" style="width:80%"></figure>

The prototype represents a self-owned, single-user meditation space. This functionality was chosen because of its simplicity. The smart contracts holding funds of no1s1 and controlling the logic around revenue and access mechanisms live on the [Ethereum](https://ethereum.org/en/) blockchain. no1s1 earns money through selling access. The prototype has solar panels to generate electricity, but can also be connected to the electricity grid. For more detailed information, we refer here to the listed resources below.

*Please note:* The project is under active development and therefore the functionality is consistently expanded. Please read the documentation inside the code folders for more information.

### Resources

For the curious reader we list here resources about this no1s1 prototype.

| Recommended resources:  |
| ----------- |
| [no1s1.space](https://no1s1.space) is the main project site to interact with the no1s1 smart contracts  |
| JJ Hunhevicz, H Wang, L Hess, DM Hall; *"no1s1 - A Blockchain-Based DAO Prototype for Autonomous Space"*; [EC<sup>3</sup> Proceedings](https://ec-3.org/publications/conferences/2021/paper/?id=185), [Conference Video](https://youtu.be/iyz45BHiRrc) ; 2021|
| H Wang, J Hunhevicz, DM Hall; *"What if properties are owned by no one or everyone? Foundations of blockchain enabled engineered ownership"*; [EC<sup>3</sup> Proceedings](http://www.doi.org/10.35490/EC3.2022.213), [Conference Video](https://www.youtube.com/watch?v=JFbBB8GSObI) ; 2022|
| [A small house raises big questions](https://ethz.ch/en/news-and-events/eth-news/news/2021/10/a-small-house-raises-big-questions.html), ETH News Article, October 2021 |
| [What happens when buildings own and manage themselves?](https://www.ey.com/en_ch/strategy/what-happens-when-buildings-own-and-manage-themselves), EY Parthenon, October 2021 |

| Further resources:  |
| ----------- |
| [From no1s1, a Self-Owning House, to Decentralized Autonomous Spaces](https://www.youtube.com/watch?v=LKWg7UzarLI), Web3 Gallery - A Glimpse into the Future, July 2022 |
| no1s1 attended [World Economic Forum](https://ethz.ch/en/the-eth-zurich/global/eth-global-news-events/2021/12/rethinking-living-exhibition.html) 2022 in Davos, [Exhibition Video](https://vimeo.com/6.578055e+08), May 2022 |
| no1s1 was featured in [SRF Panorama](https://www.srf.ch/play/radio/redirect/detail/8cacb877-d003-495f-8396-78a8d82f1c08), March 2022 |
| [Schweiz Aktuell](https://www.srf.ch/play/tv/schweiz-aktuell/video/ideen-labor-fuer-studierende?urn=urn:srf:video:652dfc9b-217d-402f-9d1e-9d4ee0db6557) featured an interview on no1s1 live at a Student Project House, November 2021 |
| Livestream with [Engineering ArchiTECHure](https://www.youtube.com/watch?v=Yh_8DTkG1dQ) on our research and prototype implementation, October 2021 |
| [Vom Warenkorb ins Blockchain-Haus: So haben wir no1s1 ausgestattet](https://www.digitec.ch/de/page/vom-warenkorb-ins-blockchain-haus-so-haben-wir-no1s1-ausgestattet-21619), Digitec Galaxus, October 2021 |

## Code

This repo contains code for the no1s1 prototype. It is structured into folders related to the different technical aspects of the prototype. Please read the README files inside the folders for further documentation.

```none
../no1s1
├── backend             Python scripts for the RaspberryPi of no1s1.
│   └── README          Documentation
├── contracts           Code related to the smart contracts of no1s1.
│   ├── README          Documentation
│   ├── contracts       Smart contracts
│   └── test            Test cases
├── frontend            Code for the dApp of no1s1.
│   └── README          Documentation
├── media               Pictures and videos on no1s1
├── README              Background and resources
└── LICENSE             MIT License
```
