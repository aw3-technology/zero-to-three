# Chapter 24: Technical Due Diligence

> *Last Updated: March 2026*

> **Skim This Chapter**
> - Technical due diligence is a bilateral process: founders must prepare their technical assets for scrutiny while investors must develop the competence to evaluate smart contracts, AI models, infrastructure, and team capabilities in domains where surface-level understanding is dangerously insufficient.
> - Output: a comprehensive technical DD framework including audit preparation checklists, code quality benchmarks, AI model evaluation criteria, tokenomics validation methods, and red flag identification guides for both sides of the investment table.

## In This Chapter

- Why technical due diligence in Web3 and AI differs fundamentally from traditional software DD
- The founder's playbook for preparing technical assets before investor scrutiny begins
- The investor's framework for evaluating smart contracts, AI models, and infrastructure
- How third-party auditors operate and what their reports actually tell you
- Tokenomics validation: separating sound design from unsustainable mechanics
- Team capability assessment beyond resumes and GitHub profiles
- Red flags that experienced technical evaluators never ignore
- Post-investment technical governance and ongoing oversight
- An implementation guide for building DD readiness into your company from day one

## 1. Introduction: The Technical Trust Problem

In traditional software investing, technical due diligence follows well-worn paths. An investor's technical advisor reviews the codebase, interviews the engineering team, examines the architecture, and produces a report estimating technical debt and scalability constraints. The process is imperfect but broadly understood. Both parties know the rules.

Web3 and AI ventures break those rules comprehensively. A smart contract deployed on Ethereum is simultaneously a piece of software and a financial instrument holding real assets. A machine learning model is simultaneously a product and a reflection of training data that may carry legal, ethical, and competitive implications invisible to traditional evaluation. The stakes of getting technical DD wrong have escalated accordingly: a missed vulnerability in a smart contract can drain hundreds of millions in hours, not months. A flawed AI model evaluation can lead an investor into backing a company whose core technology cannot perform as claimed once deployed beyond curated benchmarks.

The asymmetry of technical knowledge between founders and investors is wider in Web3 and AI than in almost any previous technology cycle. Many founders building in these domains have spent years developing expertise that most investors simply do not possess. This creates opportunities for both honest misunderstanding and deliberate obfuscation. The collapses and exploits of 2022 and 2023 demonstrated what happens when capital flows without adequate technical scrutiny. The industry's response has been a rapid professionalization of technical DD, but the frameworks remain fragmented and inconsistent.

This chapter provides a structured approach from both sides. For founders, it offers a preparation methodology that transforms DD from a stressful interrogation into a competitive advantage. For investors, it offers an evaluation framework that balances thoroughness with the practical constraints of deal timelines. For both, it draws on real cases where technical DD succeeded, failed, or was never conducted at all.

## 2. The Founder's Perspective: Preparing for Technical Scrutiny

### Why Preparation Is a Strategic Advantage

Founders who treat technical DD as an obstacle to endure are making a category error. Well-prepared technical documentation and clean codebases do not merely satisfy investor requirements; they accelerate deal timelines, increase valuations, and reduce the negotiating leverage that investors gain from identifying undisclosed technical problems.

The preparation process itself is valuable independent of fundraising. Organizing your codebase for external review forces you to confront technical debt you may have been ignoring. Documenting your architecture requires you to articulate design decisions that may have been made implicitly. Cataloging your dependencies reveals supply chain risks you may not have considered.

### The Technical Data Room

A well-structured technical data room should contain the following, organized for accessibility:

**Architecture Documentation:**
- System architecture diagrams with clear component boundaries
- Data flow diagrams showing how information moves through the system
- API documentation for all external and internal interfaces
- Infrastructure topology including cloud providers, regions, and redundancy
- For Web3: smart contract architecture showing inheritance hierarchies and upgrade patterns

**Code Quality Evidence:**
- Repository structure with clear README files and contribution guidelines
- Test coverage reports with both unit and integration test metrics
- CI/CD pipeline configuration demonstrating automated quality gates
- Static analysis reports from tools appropriate to your stack
- For Web3: formal verification results if applicable, audit reports from recognized firms
- For AI: model cards documenting training data, evaluation metrics, known limitations

**Security Posture:**
- Previous audit reports with remediation evidence
- Bug bounty program details and historical findings
- Incident response documentation for any past security events
- Dependency audit results showing known vulnerability status
- Access control policies and key management procedures

**Team Technical Evidence:**
- Open-source contributions by team members with context
- Technical blog posts, conference talks, or research publications
- Relevant certifications or specialized training
- Prior technical leadership roles and outcomes

### Common Founder Mistakes in DD Preparation

Several patterns reliably damage founder credibility during technical DD:

**Over-reliance on vanity metrics.** Claiming 95 percent test coverage while the tests themselves are superficial or test only trivial code paths. Experienced evaluators will read the actual tests, not just the coverage number.

**Hiding technical debt.** Every early-stage company has technical debt. Attempting to conceal it suggests either dishonesty or a lack of awareness. The better approach is to document known debt, explain why it was incurred (usually for valid speed-to-market reasons), and present a remediation plan.

**Exaggerating AI capabilities.** Presenting cherry-picked model outputs as representative performance. Showing benchmark results on carefully curated test sets while avoiding discussion of real-world deployment performance. Investors who have been burned by this pattern are increasingly bringing their own evaluation datasets.

**Obscuring smart contract risks.** Minimizing the implications of centralized admin keys, upgrade mechanisms, or oracle dependencies. These are not inherently disqualifying, but hiding them is.

## 3. The Investor's Perspective: What to Evaluate and How

### Building Technical Evaluation Competence

Investors evaluating Web3 and AI companies face a fundamental capability challenge. The domains are sufficiently specialized that generalist technical advisors frequently miss critical issues. The most effective investor teams employ one of three models:

**In-house specialists.** Firms like Paradigm and a16z crypto maintain dedicated engineering teams who can conduct primary technical evaluation. This is the gold standard but requires significant ongoing investment.

**Retained expert networks.** Many mid-tier funds maintain relationships with independent smart contract auditors, ML engineers, and infrastructure architects who can be engaged for specific deal evaluations. This provides flexibility but requires careful management to avoid conflicts of interest.

**Third-party DD firms.** A growing number of firms specialize in technical DD for Web3 and AI investments. These range from established security firms that have expanded into DD (Trail of Bits, OpenZeppelin) to newer entrants focused specifically on investor-side evaluation.

### Smart Contract Evaluation Framework

When evaluating a Web3 project's smart contracts, investors should examine several dimensions:

**Access Control and Privilege.**
- Who holds admin keys and what powers do they grant?
- Are there timelocks on administrative functions?
- Is there a multisignature requirement for critical operations?
- Can contracts be upgraded, and if so, through what governance mechanism?

**Economic Logic.**
- Do the mathematical models in the contracts correctly implement the claimed tokenomics?
- Are there edge cases in fee calculations, reward distributions, or liquidation logic?
- How does the protocol behave under extreme market conditions (90 percent price drops, zero liquidity)?

**External Dependencies.**
- Which oracles does the protocol rely on, and what happens if they fail or are manipulated?
- Are there cross-chain dependencies, and what bridge mechanisms are used?
- What happens if a dependent protocol is exploited or becomes unavailable?

**Code Quality Indicators.**
- Is the code well-documented with NatSpec or equivalent commenting?
- Are there comprehensive test suites including fuzz testing and invariant testing?
- Has formal verification been applied to critical components?
- Is the deployment process documented and reproducible?

### AI Model Evaluation Framework

Evaluating AI-centric companies requires a different but equally rigorous approach:

**Data Quality and Provenance.**
- What training data was used, and does the company have clear rights to it?
- How was the data cleaned, labeled, and validated?
- Are there known biases in the training data, and how have they been addressed?
- What is the data refresh strategy for maintaining model relevance?

**Model Performance.**
- What benchmarks were used, and are they appropriate for the claimed use case?
- How does performance on curated benchmarks compare to real-world deployment metrics?
- What are the failure modes, and how gracefully does the model degrade?
- Has the model been evaluated by independent third parties?

**Competitive Moat.**
- Is the model's advantage based on architecture, data, or both?
- How defensible is the data advantage against competitors with more compute?
- What happens when foundation model providers release competing capabilities?
- Is there proprietary training methodology that creates sustainable differentiation?

**Deployment and Operations.**
- What is the inference cost per query, and how does it scale?
- What latency characteristics does the model exhibit in production?
- How is model drift detected and addressed?
- What monitoring and observability infrastructure exists?

## 4. Case Studies in Technical Due Diligence

### Case Study 1: FTX — The Due Diligence That Was Never Done

The collapse of FTX in November 2022 represents perhaps the most consequential failure of technical due diligence in the history of venture capital. FTX raised approximately $1.8 billion from investors including Sequoia Capital, Paradigm, and the Ontario Teachers' Pension Plan at a peak valuation of $32 billion. The subsequent bankruptcy revealed that even basic technical DD had been largely absent.

The technical failures were extraordinary in their simplicity. FTX operated without standard financial controls software. Customer funds were commingled with Alameda Research's trading operations through a backdoor in the accounting system, reportedly implemented through a single line of code that exempted Alameda from the auto-liquidation engine applied to every other counterparty. The exchange's risk management was effectively nonexistent. There was no independent board, no chief risk officer, and no audit committee overseeing technology operations.

What makes the FTX case instructive for technical DD is not the complexity of the fraud but its detectability. A competent technical evaluation would have revealed the absence of basic software engineering practices: no proper separation of concerns between exchange operations and proprietary trading, no access control logs for customer fund movements, no automated reconciliation between reported balances and actual reserves. These are not sophisticated vulnerabilities requiring specialized blockchain expertise. They are fundamental software engineering failures that any experienced technical evaluator would identify.

The lesson for investors is uncomfortable but important: technical DD requires actually examining the technology. Several of FTX's investors later acknowledged that their diligence had focused primarily on market opportunity, team reputation, and financial projections. The technology was assumed to work because the platform appeared to function and because SBF's reputation made scrutiny feel unnecessary. That assumption proved to be catastrophically expensive.

### Case Study 2: Euler Finance — When Audits Provide Genuine Value

Euler Finance, an Ethereum-based lending protocol, experienced a $197 million flash loan exploit in March 2023. While the exploit itself was damaging, the case illustrates both the value and the limitations of the audit process.

Euler had invested significantly in security prior to the exploit. The protocol had been audited multiple times by reputable firms, had an active bug bounty program, and employed formal verification on core components. The vulnerability that was exploited involved a specific interaction between the protocol's donation function and its liquidation mechanism, a path that auditors had not identified because it required a particular sequence of operations across multiple transactions.

What makes Euler instructive is what happened after the exploit. Because the protocol had been well-architected with clearly documented upgrade mechanisms and a responsive security team, the Euler team was able to negotiate with the attacker and recover the majority of the stolen funds within three weeks. The protocol's strong technical foundation, including comprehensive event logging, clear governance processes, and established relationships with security researchers, enabled a response that would have been impossible for a less rigorously engineered system.

For investors conducting technical DD, Euler demonstrates that audits are necessary but not sufficient. The right question is not "has this been audited?" but rather "what is the protocol's security posture across multiple dimensions, and what happens when something goes wrong despite those precautions?" A protocol with thorough audits, active monitoring, a bug bounty program, incident response plans, and upgrade mechanisms represents a fundamentally different risk profile than one with a single audit report and no further security infrastructure.

### Case Study 3: Sky Mavis and the Ronin Bridge — Validator Architecture Under Scrutiny

In March 2022, the Ronin Bridge operated by Sky Mavis (the Vietnamese studio behind Axie Infinity) was exploited for approximately $625 million, making it one of the largest cryptocurrency thefts in history. The exploit was not a smart contract vulnerability in the traditional sense. It was an architectural failure in the bridge's validator set.

The Ronin Bridge relied on a set of nine validators to confirm cross-chain transactions, requiring five of nine signatures to approve a withdrawal. Sky Mavis controlled four of these validators directly. A fifth validator was controlled by the Axie DAO, which had temporarily granted Sky Mavis the authority to sign transactions on its behalf during a period of high network congestion. This delegation was never revoked. The attacker compromised Sky Mavis's systems through a social engineering attack on an employee and gained access to all five required signing keys.

From a technical DD perspective, the Ronin exploit reveals the importance of evaluating governance architecture alongside code quality. The smart contracts themselves functioned as designed. The vulnerability was in the design itself: a validator set that was insufficiently decentralized, with a single organization controlling a majority of signing authority. A thorough technical evaluation would have identified this concentration risk by examining the validator key management procedures and the governance structure of the bridge, areas that many code-focused audits do not cover.

The case also demonstrates the importance of evaluating operational security alongside software security. The initial compromise vector was social engineering, not a code exploit. Technical DD that focuses exclusively on code review while ignoring the operational security environment provides an incomplete picture of risk.

### Case Study 4: Cohere — AI Model Evaluation in Practice

Cohere, a Toronto-based AI company focused on enterprise natural language processing, has undergone multiple rounds of technical DD as part of its fundraising journey from seed through its Series C in 2023. The company's experience illustrates how AI model evaluation has matured as investors have become more sophisticated.

In its early fundraising rounds, Cohere's technical DD primarily involved demonstrating model performance on standard NLP benchmarks and showing that the team had relevant expertise from their backgrounds at Google Brain. As the company matured and the competitive landscape for large language models intensified, the DD process became significantly more rigorous.

Later-stage investors brought independent ML engineers to evaluate Cohere's models on custom benchmarks relevant to the enterprise use cases the company was targeting. These evaluations went beyond accuracy metrics to examine inference latency, cost per query at scale, model behavior on adversarial inputs, and the company's fine-tuning pipeline for customer-specific deployments. Investors also examined Cohere's data provenance practices, which had become a significant legal risk factor as lawsuits over AI training data proliferated.

The Cohere case demonstrates that AI technical DD must evolve with the maturity of the company and the competitive landscape. Early-stage evaluation appropriately focuses on team capability and architectural soundness. Later-stage evaluation must rigorously test claims about performance, cost, and scalability under realistic deployment conditions.

### Case Study 5: Solv Protocol — Tokenomics Validation in Beijing's DeFi Ecosystem

Solv Protocol, a Beijing-founded decentralized finance platform focused on creating and trading financial vouchers (semi-fungible tokens representing various financial instruments), provides an instructive case in tokenomics validation during technical DD.

When Solv raised its Series A, investors needed to evaluate a novel token mechanism: voucher tokens that represented claims on underlying assets with customizable parameters for vesting schedules, conditional redemption, and transferability. The technical DD process required evaluating not just whether the smart contracts correctly implemented the claimed functionality, but whether the tokenomics model was economically sustainable under various market conditions.

The evaluation involved stress-testing the protocol's economic model through simulation: what happens when a large percentage of voucher holders attempt simultaneous redemption? How do the protocol's fee mechanisms behave when underlying asset prices are highly volatile? Are there arbitrage loops that could be exploited to extract value from the protocol at the expense of other participants?

Solv's technical team had prepared for this level of scrutiny by building economic simulation tools that could model protocol behavior under hundreds of market scenarios. This preparation accelerated the DD process and increased investor confidence. The case illustrates that for DeFi protocols, technical DD must encompass economic modeling alongside code review, and that founders who invest in simulation infrastructure gain significant advantages in the fundraising process.

## 5. Code Quality Metrics and Infrastructure Assessment

### Quantitative Code Quality Indicators

While no single metric captures code quality comprehensively, several quantitative indicators are useful in aggregate:

**Test Coverage:** Not merely the percentage of lines covered, but the quality of test assertions. For smart contracts, look for fuzz testing coverage and invariant tests alongside unit tests. For AI systems, look for evaluation suites that test edge cases and failure modes alongside standard benchmarks. Industry benchmarks suggest that production-quality smart contracts should demonstrate at least 90 percent line coverage with meaningful assertions, while AI systems should have evaluation suites covering at least the documented use cases plus known failure modes.

**Cyclomatic Complexity:** High complexity in critical code paths (smart contract functions handling asset transfers, core model inference pipelines) indicates elevated risk. Look for complexity scores below 10 in critical functions.

**Dependency Health:** The number and status of third-party dependencies, including whether they are actively maintained, whether known vulnerabilities exist, and whether the project has a process for dependency updates. In Web3, forked dependencies that are not kept in sync with upstream create particularly insidious risks.

**Documentation Ratio:** The ratio of documentation to code. While not a precise quality indicator, codebases with essentially no documentation reliably correlate with other quality problems.

### Infrastructure Scalability Assessment

For Web3 projects, infrastructure evaluation should examine:
- Node infrastructure: self-hosted versus third-party providers (Infura, Alchemy), redundancy, geographic distribution
- Indexing infrastructure: subgraph reliability, custom indexing solutions, data consistency guarantees
- Frontend infrastructure: decentralization of the user interface, IPFS hosting, DNS dependencies

For AI projects, infrastructure evaluation should examine:
- Training infrastructure: GPU/TPU allocation, cost management, reproducibility of training runs
- Inference infrastructure: latency percentiles (p50, p95, p99), throughput capacity, auto-scaling behavior
- Data infrastructure: storage architecture, data pipeline reliability, backup and disaster recovery

## 6. Team Capability Assessment

### Beyond Resumes: Evaluating Technical Teams

Technical team evaluation in Web3 and AI requires methods that go beyond traditional credential checking:

**Open-Source Contribution Analysis.** For Web3 teams, examine contributions to relevant open-source projects. Look not just at volume but at the nature of contributions: are they fixing critical bugs, implementing complex features, or making cosmetic changes? GitHub contribution graphs can be misleading; actual code review is essential. Pay attention to how team members interact in public code review discussions, as this reveals communication quality, technical depth, and collaborative capability.

**Technical Interview Quality.** The best technical DD processes include structured technical conversations with individual team members, not just the CTO. These conversations should probe not for textbook knowledge but for the practical judgment that comes from experience: how the team approaches architectural trade-offs, how they handle disagreements about technical direction, and how they respond to genuine uncertainty.

**Organizational Design.** How the engineering team is structured reveals as much as individual capability. Look for clear ownership of critical systems, sensible on-call rotations, and decision-making processes that balance speed with safety. Teams that cannot articulate who is responsible for what in their own system are usually in deeper trouble than they realize.

## 7. Tokenomics Validation

### Structural Evaluation Framework

For any project with a token component, technical DD must include rigorous tokenomics evaluation:

**Supply Mechanics:** Examine emission schedules, inflation rates, and any programmatic supply changes. Verify that the smart contract implementation matches the documented tokenomics. Common discrepancies include rounding errors in emission calculations and off-by-one errors in vesting schedules that compound over time.

**Value Capture:** How does the token capture value from the protocol's economic activity? Tokens that rely solely on speculative demand without a clear value accrual mechanism are structurally fragile. Look for revenue-sharing mechanisms, burn mechanics, or staking requirements that create organic demand.

**Governance Alignment:** If the token grants governance power, examine whether the governance structure creates genuine decentralization or concentrates power in the hands of the team and early investors. Voting participation rates, proposal thresholds, and timelock durations are all measurable indicators of governance health.

**Simulation Results:** Credible tokenomics should be supported by agent-based simulation showing protocol behavior under various market conditions. Protocols that have not modeled their own economics are operating on assumptions that may not survive contact with reality.

## 8. Red Flags in Technical Due Diligence

Experienced technical evaluators maintain a mental checklist of warning signs that warrant deeper investigation or outright concern:

- **Refusal to share code before term sheet.** While some founders cite competitive concerns, legitimate projects can share code under NDA. Persistent refusal often indicates that the code will not survive scrutiny.
- **Single points of failure in key management.** One person holding all admin keys with no multisignature, no timelock, and no documented succession plan.
- **Audit reports with unresolved critical findings.** Particularly when the team has chosen not to remediate critical or high-severity findings without a documented rationale.
- **Claims of proprietary AI without evidence.** Teams claiming novel model architectures while using off-the-shelf foundation models with minimal fine-tuning.
- **Unusually high team turnover in engineering.** Particularly when departing engineers are senior and their replacements are more junior.
- **No monitoring or alerting infrastructure.** Systems running in production without observability tools suggest an engineering culture that does not prioritize operational reliability.
- **Mismatch between claimed scale and infrastructure.** A protocol claiming millions of users while running on a single cloud instance, or an AI company claiming massive model training while spending minimal amounts on compute.
- **Forked code with no upstream tracking.** Projects that forked a protocol or model months ago and have not incorporated upstream security patches or improvements.

## 9. Third-Party Auditors: The Landscape

### Leading Firms and Their Specializations

The security audit landscape for Web3 has matured significantly:

**Trail of Bits.** Based in New York, Trail of Bits is widely regarded as one of the most rigorous security firms in the space. Their methodology combines manual review with custom tooling (including their Slither static analysis framework and Echidna fuzzer). They are known for thorough reports that examine architectural concerns alongside code-level vulnerabilities.

**OpenZeppelin.** Originally known for their widely-used smart contract library, OpenZeppelin's audit practice has become one of the most active in the industry. They have audited many of the largest DeFi protocols and maintain deep expertise in Solidity and EVM-based systems.

**Certora.** Specializing in formal verification, Certora applies mathematical proof techniques to smart contract security. Their approach is complementary to traditional auditing: where auditors look for specific vulnerabilities, formal verification proves that certain classes of bugs cannot exist. The Certora Prover has been used to verify critical components of protocols including Aave and Compound.

### What Audit Reports Actually Tell You

A common mistake among both founders and investors is treating audit reports as binary pass/fail assessments. In reality, audit reports are nuanced documents that require careful interpretation:

- The scope of the audit matters enormously. An audit of a protocol's core lending contracts does not cover the oracle integration, the governance module, or the frontend.
- Severity classifications vary across firms. A "medium" finding at one firm might be classified as "high" at another.
- Audit reports reflect the state of the code at a specific point in time. Subsequent changes may introduce new vulnerabilities or re-introduce remediated ones.
- The absence of findings does not mean the absence of vulnerabilities. It means that the auditors did not find vulnerabilities within the scope, methodology, and time constraints of their engagement.

## 10. Post-Investment Technical Governance

Technical DD should not end at the investment decision. Effective post-investment technical governance includes:

**Regular Technical Reviews.** Quarterly reviews of the technology stack, security posture, and engineering team health. These should be conducted by someone with relevant technical expertise, not delegated to board members without engineering backgrounds.

**Incident Response Requirements.** Clear expectations for how the company will communicate and respond to security incidents, including notification timelines, severity classification, and remediation tracking.

**Audit Cadence.** Establishing expectations for ongoing security audits, particularly before major protocol upgrades or product launches.

**Key Person Dependencies.** Monitoring concentration of critical knowledge in individual team members and ensuring that knowledge transfer and documentation practices mitigate key-person risk.

**Technical Milestone Tracking.** Establishing measurable technical milestones as part of the investment terms, with clear definitions of what constitutes completion.

## 11. Implementation Guide: Building DD Readiness from Day One

### For Founders

**Month 1-3: Establish Foundations**
- Set up CI/CD pipelines with automated testing and static analysis
- Implement code review requirements (minimum one reviewer for all changes)
- Begin maintaining architecture documentation as a living document
- Establish access control policies and key management procedures

**Month 4-6: Build Security Posture**
- Conduct initial internal security review or engage an auditor for critical components
- Launch a bug bounty program, even at modest reward levels
- Implement monitoring and alerting for production systems
- Document incident response procedures

**Month 7-12: Prepare for Scrutiny**
- Organize the technical data room with all materials described in Section 2
- Conduct a mock DD exercise with a trusted technical advisor
- Address identified gaps in documentation, testing, or security
- Prepare clear narratives for known technical debt and remediation plans

### For Investors

**Pre-Engagement**
- Identify the technical expertise required for this specific evaluation (smart contract, ML, infrastructure)
- Prepare evaluation frameworks customized to the company's domain
- Request technical data room access early in the diligence process

**During Evaluation (Weeks 1-3)**
- Review architecture documentation and identify questions
- Conduct code review of critical components
- Interview engineering team members individually
- Engage third-party specialists for areas requiring deep domain expertise
- For Web3: review audit reports, examine on-chain data, test contract behavior
- For AI: evaluate model performance on independent benchmarks, examine data provenance

**Synthesis (Week 4)**
- Compile findings into a structured assessment covering code quality, security, architecture, team, and economic model
- Classify issues by severity and remediation feasibility
- Present findings with clear recommendations: proceed, proceed with conditions, or decline

---

## Checklist

- [ ] Technical data room is organized with architecture docs, code quality evidence, security materials, and team documentation
- [ ] All smart contracts have been audited by at least one reputable firm, with findings remediated or documented
- [ ] AI models have been evaluated on benchmarks relevant to actual deployment use cases, not just standard academic benchmarks
- [ ] Test coverage exceeds 90 percent for critical code paths with meaningful assertions
- [ ] Key management uses multisignature with documented access control policies
- [ ] Infrastructure has been load-tested to at least 3x current peak demand
- [ ] Tokenomics have been validated through agent-based simulation under adverse conditions
- [ ] Team capability has been assessed through contribution analysis, technical interviews, and organizational design review
- [ ] Known technical debt is documented with clear remediation timelines
- [ ] Post-investment governance structure includes technical review cadence, incident response requirements, and milestone tracking
- [ ] Red flag checklist has been applied and any identified concerns have been investigated
- [ ] Third-party audit reports have been interpreted in context (scope, timing, methodology) rather than treated as pass/fail

## Exercises

1. **Technical Data Room Audit.** Take your current codebase and attempt to assemble a complete technical data room using the framework in Section 2. Identify the gaps. Which materials exist but are outdated? Which do not exist at all? Create a prioritized plan to address the top five gaps within 30 days.

2. **Red Flag Self-Assessment.** Review the red flags listed in Section 8 and honestly evaluate whether any apply to your own company. For each that does, write a one-paragraph explanation of why it exists and a concrete plan for remediation. Share this assessment with a trusted advisor and solicit their candid feedback.

3. **Mock Due Diligence.** Engage a technically competent friend or advisor to conduct a two-day mock technical DD of your company. Provide them with your data room materials and ask them to produce a findings report. Review the report with your engineering team and incorporate the findings into your DD preparation plan.

4. **Tokenomics Stress Test.** If your project includes a token, build a simple simulation (even a spreadsheet-based model) that models your tokenomics under three scenarios: bull market (3x price increase, high participation), steady state (stable price, moderate participation), and bear market (80 percent price decline, low participation). Identify which scenario reveals the most concerning behavior and develop mitigation strategies.

5. **Audit Report Interpretation.** Obtain three publicly available audit reports from reputable firms (many DeFi protocols publish theirs). Read each report and for each finding, assess: would you have identified this issue through your own review process? What does this tell you about the gaps in your security evaluation methodology?

## Sources

- Trail of Bits, "Building Secure Smart Contracts," 2023 Edition, https://building-secure-contracts.com
- OpenZeppelin, "Smart Contract Security Guidelines," 2024
- Certora, "Formal Verification for DeFi Protocols," Certora Documentation, 2024
- Crunchbase, "Venture Capital Due Diligence Trends," Annual Report, 2024
- Galaxy Digital Research, "State of Crypto Venture Capital," 2024
- U.S. Securities and Exchange Commission, "Report on FTX Collapse and Investor Due Diligence Failures," 2023
- Chainalysis, "The 2023 Crypto Crime Report: DeFi Exploits and Bridge Attacks," 2023
- Euler Finance, "Post-Mortem: March 2023 Exploit and Recovery," Euler Labs Blog, 2023
- Ronin Network, "Community Alert: Ronin Bridge Exploit," Sky Mavis Blog, March 2022
- Mitchell, M. et al., "Model Cards for Model Reporting," Proceedings of the Conference on Fairness, Accountability, and Transparency, 2019
- Perez, Daniel and Livshits, Benjamin, "Smart Contract Vulnerabilities: Vulnerable Does Not Imply Exploited," USENIX Security Symposium, 2021
