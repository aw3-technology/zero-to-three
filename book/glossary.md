# Glossary

Quick-reference definitions for key terms used throughout *Zero to Three*. Terms are grouped thematically; see also the [Index](index.md) for chapter-level cross-references.

---

## Blockchain and Web3

**Blockchain:** A distributed, append-only ledger maintained by a network of nodes. Each block contains a cryptographic hash of the previous block, creating a tamper-evident chain. Relevant chapters: 04, 22, 23.

**Consensus Mechanism:** The method by which a distributed network agrees on the state of the ledger. Major types include Proof of Work (PoW), Proof of Stake (PoS), and Delegated Proof of Stake (DPoS). Relevant chapters: 04, 23.

**DAO (Decentralized Autonomous Organization):** An organization governed by smart contracts and token-holder voting rather than traditional corporate hierarchy. Governance rules are encoded on-chain, enabling transparent decision-making. Relevant chapters: 28, 34.

**DeFi (Decentralized Finance):** Financial services (lending, borrowing, trading, insurance) built on blockchain protocols without centralized intermediaries. Uses smart contracts to automate financial operations. Relevant chapters: 22, 23.

**DePIN (Decentralized Physical Infrastructure Networks):** Networks that use token incentives to coordinate the deployment and maintenance of real-world physical infrastructure (e.g., wireless networks, mapping, energy grids). Relevant chapters: 29, 40.

**Gas Fees:** Transaction costs on blockchain networks, paid to validators for processing and confirming transactions. Gas prices fluctuate based on network congestion. Relevant chapter: 23.

**Layer 1 / Layer 2:** Layer 1 refers to the base blockchain protocol (e.g., Ethereum, Bitcoin). Layer 2 refers to scaling solutions built on top of Layer 1 that handle transactions off the main chain while inheriting its security guarantees. Relevant chapters: 04, 23.

**NFT (Non-Fungible Token):** A unique, indivisible digital asset recorded on a blockchain. Unlike fungible tokens (where each unit is interchangeable), each NFT represents a distinct item with unique metadata. Relevant chapters: 22, 32.

**Oracle:** A service that provides external (off-chain) data to smart contracts on a blockchain. Oracles bridge the gap between deterministic on-chain computation and real-world information. Relevant chapter: 23.

**Protocol Layer:** The foundational rules and standards that define how participants interact within a decentralized network. Sits below the application layer and above the infrastructure layer. Building at the protocol layer creates leverage because every application built on top inherits these rules. Relevant chapters: 04, 06, 23.

**Smart Contract:** Self-executing code deployed on a blockchain that automatically enforces the terms of an agreement when predefined conditions are met. Once deployed, smart contracts operate autonomously without intermediaries. Relevant chapters: 23, 28.

**Token:** A digital asset issued on a blockchain. Can represent ownership (equity tokens), utility (access tokens), governance (voting tokens), or other rights. Distinct from cryptocurrency in that tokens are built on existing blockchains rather than maintaining their own. Relevant chapters: 05, 22.

**Tokenomics:** The economic design of a token system, including supply mechanics (minting, burning), distribution schedules, incentive structures, and value-capture mechanisms. Good tokenomics align participant behavior with network health. Relevant chapters: 05, 22.

**Web3:** The vision of a decentralized internet built on blockchain technology, where users own their data, digital assets, and identity. Emphasizes verifiable ownership, programmable assets, and distributed coordination rather than platform-controlled intermediation. Relevant chapters: 01, 04, 07.

## AI and Machine Learning

**Alignment:** Ensuring AI systems behave in accordance with human values and intentions. In a broader sense, structuring incentives, information flows, and authority so that all participants in a system work toward shared goals. Relevant chapters: 27, 46.

**Constitutional AI:** An AI training approach (pioneered by Anthropic) where the model is guided by a set of principles ("constitution") rather than purely human feedback. Aims to make AI systems more predictable and aligned with stated values. Relevant chapter: 27.

**Foundation Model:** A large AI model trained on broad data that can be adapted (fine-tuned) for many downstream tasks. Examples include GPT, Claude, and open-weight models like Llama and Mistral. Relevant chapters: 04, 27.

**Frontier Model:** The most capable AI models at any given time, typically trained with the largest compute budgets and newest architectures. These models define the state of the art. Relevant chapters: 04, 27.

**LLM (Large Language Model):** An AI model trained on vast text corpora to generate, understand, and reason about language. Modern LLMs (GPT-4, Claude, Gemini) exhibit emergent capabilities including code generation, mathematical reasoning, and multi-step planning. Relevant chapters: 04, 18, 27.

**Mixture of Experts (MoE):** An architecture that routes each input to a subset of specialized "expert" sub-networks rather than activating the entire model. Enables larger total model capacity while keeping per-inference compute costs manageable. Relevant chapter: 27.

**Open-Weight Model:** An AI model whose trained parameters (weights) are publicly released, allowing anyone to run, fine-tune, or build upon it. Distinct from "open source" in that training code and data may not be included. Relevant chapters: 27, 04.

**RAG (Retrieval-Augmented Generation):** A technique that combines AI text generation with information retrieval from external knowledge bases, allowing models to access up-to-date or domain-specific information beyond their training data. Relevant chapter: 27.

## Business and Strategy

**Blitzscaling:** A growth strategy that prioritizes speed of scaling over efficiency, accepting short-term losses for long-term market dominance. Coined by Reid Hoffman. Effective when network effects create winner-take-most dynamics; risky when capital dries up. Relevant chapters: 05, 16.

**DX Moat (Developer Experience Moat):** A competitive advantage created by making a platform so easy and pleasant for developers to build on that switching costs become prohibitive. The quality of documentation, tooling, SDKs, and community support creates compounding lock-in. Relevant chapters: 20, 31.

**Flywheel:** A self-reinforcing business cycle where each component of the system accelerates the others. Example: more users attract more developers, who build more apps, which attract more users. Relevant chapters: 31, 34.

**Governance:** The systems and processes by which decisions are proposed, debated, approved, and enacted within an organization or protocol. Can be on-chain (smart contract voting), off-chain (forum discussions, committee decisions), or hybrid. Relevant chapters: 28, 34, 36.

**Network Effects:** The phenomenon where a product or service becomes more valuable as more people use it. Direct network effects (each user adds value for other users) and indirect network effects (more users attract complementary offerings). Relevant chapters: 31, 33, 34.

**Platform Economics:** The economic dynamics of multi-sided platforms that create value by facilitating interactions between distinct user groups (e.g., developers and end users, buyers and sellers). Relevant chapters: 06, 34, 35.

**Product-Market Fit:** The state where a product satisfies strong market demand, evidenced by organic growth, high retention, and willingness to pay. In Web3, extends to "protocol-market fit" where the incentive design matches participant motivations. Relevant chapters: 11, 24.

**Unit Economics:** The revenue and cost analysis for a single unit of a product or service (one user, one transaction, one subscription). Positive unit economics means each additional unit contributes to profit rather than increasing losses. Relevant chapters: 05, 16.

**ZIRP (Zero Interest Rate Policy):** A central bank policy of maintaining near-zero interest rates, as practiced by the US Federal Reserve from 2008-2015 and 2020-2022. Created abundant cheap capital that inflated venture valuations and enabled growth-over-profit strategies. Its end in 2022 triggered a reset in startup economics. Relevant chapters: 05, 16.

## Framework Terms

**Zero (Stage):** The foundational stage of the Zero to Three framework. Focuses on founder mindset, resilience, asymmetric insight, and personal development. The question at this stage: "What do I uniquely see that others don't?" Relevant chapters: 11-18.

**One (Stage):** The building stage. Creating a working product, protocol, or service that solves a real problem. Corresponds to Thiel's "zero to one" concept of vertical innovation. The question: "Does this actually work and create value?" Relevant chapters: 19-31.

**Two (Stage):** The traction stage. Building community, establishing trust, and creating network effects. Governance design becomes critical. The question: "Do people trust this enough to depend on it?" Relevant chapters: 32-35.

**Three (Stage):** The system leadership stage. Creating infrastructure and ecosystems that enable others to build. The founder becomes a steward rather than a controller. The question: "Can this thrive without me?" Relevant chapters: 36-39.

---

*Terms not found here? Check the [Index](index.md) for chapter-level references, or consult the introduction's [Short Glossary](02-introduction.md#short-glossary) for the five most essential terms.*
