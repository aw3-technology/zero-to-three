# Chapter 53: Technical Due Diligence

> *Last Updated: March 2026*

> **Difficulty: Advanced** -- Prerequisite Knowledge: Familiarity with software development practices, basic understanding of smart contract architecture, and awareness of AI/ML model development workflows. Chapters 04 (Technical Paradigm Shift), 20 (Technology Decisions), and 23 (Web3 Architecture and Security) provide useful context.

> **Non-Technical Summary**
>
> Technical due diligence is the process by which investors evaluate whether a company's technology actually works, can scale, and is defensible---and the process by which founders prepare to withstand that scrutiny. In Web3 and AI, this process has become dramatically more complex and consequential than in traditional software investing. Key takeaways: (1) founders who prepare for technical due diligence before investors ask are better positioned to negotiate favorable terms; (2) the absence of rigorous technical due diligence has led to catastrophic failures in Web3 and AI; (3) third-party audits, while essential, are not sufficient on their own---they must be complemented by internal discipline and ongoing technical governance.

## 1. Introduction: Why Technical Due Diligence Has Changed

In traditional venture investing, technical due diligence was often a secondary concern. A seasoned CTO advisor could spend an afternoon reviewing a SaaS application's architecture and provide a credible assessment. The stakes were bounded: a poorly architected monolith could be refactored, and technical debt, while costly, rarely threatened existential destruction.

Web3 and AI have fundamentally altered these dynamics. A vulnerability in a smart contract is not a bug to be patched in the next sprint---it is a potential mechanism for the instantaneous, irreversible loss of hundreds of millions of dollars. An AI model trained on poisoned data is not merely a product deficiency---it is a regulatory liability and a legal exposure that can destroy a company before it reaches product-market fit.

The consequences of inadequate due diligence have been demonstrated with painful clarity. The collapse of FTX revealed billions invested in an organization whose technical infrastructure would have failed a cursory independent review. The Wormhole bridge exploit of February 2022 resulted in $320 million in losses through a vulnerability a thorough audit would likely have identified. Conversely, protocols that invested in security audits and formal verification---such as Uniswap and Aave---have operated through multiple market cycles without critical exploits.

This chapter addresses technical due diligence from both sides of the table: for founders preparing for investor scrutiny, and for investors evaluating the technical merits and risks of Web3 and AI ventures. The central thesis is straightforward: in an era where technology is itself the product, the asset, and often the regulatory surface area, technical due diligence is no longer a checkbox in the investment process. It is the investment process.

## 2. The Founder's Perspective: Preparing for Technical Scrutiny

### Building a Diligence-Ready Technical Organization

The most effective approach to technical due diligence is not to prepare for it as a discrete event but to build an organization whose technical practices would withstand scrutiny at any time. This requires discipline across several dimensions.

**Code Quality and Documentation:**
- Maintain consistent coding standards enforced through automated linting and formatting
- Require meaningful code reviews for all changes, with review comments preserved in version control
- Document architectural decisions through Architecture Decision Records (ADRs) that capture not only what was decided but why alternatives were rejected
- Maintain up-to-date API documentation and system architecture diagrams
- Keep dependency lists current and flag known vulnerabilities through automated scanning

**Testing and Verification:**
- Maintain test coverage above 80 percent for critical paths, with particular emphasis on edge cases and failure modes
- Implement continuous integration pipelines that run the full test suite on every commit
- For smart contracts: supplement unit tests with property-based testing and formal verification of critical invariants
- For AI systems: maintain reproducible evaluation pipelines with versioned datasets and benchmark suites
- Document known limitations and failure modes honestly rather than concealing them

**Security Posture:**
- Conduct internal security reviews on a regular cadence, not only before fundraising
- Maintain a vulnerability disclosure process and demonstrate responsiveness to reported issues
- For Web3: engage external auditors early and address findings systematically, maintaining a public record of audits and remediation
- For AI: document model safety testing, red-teaming exercises, and bias assessments
- Implement role-based access controls and audit logging for all production systems

### The Technical Narrative

Beyond the mechanics of code quality, founders must be prepared to articulate a coherent technical narrative that addresses several critical questions investors will ask.

**Why this architecture?** Investors want to understand not only what you built but why you chose this approach over alternatives. A founder who can explain the trade-offs between a rollup-based architecture and an appchain, or between fine-tuning an existing foundation model and training a custom model from scratch, demonstrates the kind of technical judgment that predicts future decision-making quality.

**What is the technical moat?** In Web3, moats may derive from network effects, liquidity depth, or novel cryptographic techniques. In AI, they may derive from proprietary training data, specialized model architectures, or inference optimization techniques. Founders must articulate specifically why their technical approach is difficult to replicate and how that difficulty compounds over time.

**What are you worried about?** Counterintuitively, founders who can clearly articulate the technical risks they face and their mitigation strategies create more investor confidence than those who claim everything is under control. Sophisticated investors know that every technical system has vulnerabilities; the question is whether the team understands them.

### Case Study: How a DeFi Protocol Used Pre-Emptive Audits as a Fundraising Advantage

In late 2022, a DeFi lending protocol called Euler Finance had already undergone multiple rounds of security audits and had established a reputation for technical rigor. The protocol had engaged firms including Halborn and Sherlock, maintained an active bug bounty program through Immunefi, and published detailed post-audit reports documenting how each finding was addressed. When approaching Series B investors, the Euler team presented a comprehensive security dossier that included not only audit results but a chronological record of how their security practices had matured over time.

This proactive approach accomplished several objectives simultaneously. First, it compressed the due diligence timeline. Investors who might have spent weeks arranging their own technical reviews could instead evaluate an existing body of evidence. Second, it shifted the conversation from defensive justification to collaborative problem-solving---investors engaged with the team on forward-looking security architecture rather than interrogating past decisions. Third, it served as a powerful signal of organizational maturity. The willingness to invest substantial resources in security before being asked to do so indicated a team that understood the stakes of operating a protocol that held user funds.

The lesson for founders extends beyond security audits. Any dimension of technical quality that can be documented and presented proactively---performance benchmarks, scalability testing results, disaster recovery procedures---removes uncertainty from the investor's evaluation and demonstrates the kind of operational discipline that correlates with long-term success. Critically, however, the Euler case also carries a sobering addendum: despite its strong audit history, Euler Finance suffered a $197 million flash loan exploit in March 2023. The vulnerability involved complex interactions between multiple protocol features that were not fully captured by the audits performed. The attacker later returned most of the funds, but the incident underscored that audits, however thorough, represent a point-in-time assessment and cannot guarantee future security. This reality reinforces rather than undermines the importance of continuous, multi-layered security practices---a theme we return to throughout this chapter.

## 3. The Investor's Perspective: What to Evaluate

### Structuring the Technical Review

Technical due diligence for Web3 and AI companies requires a structured methodology that goes beyond subjective assessments of code quality. The following framework organizes the evaluation into five domains, each with specific evaluation criteria.

**Domain 1: Architecture and Design.** Appropriateness of architectural choices for the stated problem. Scalability characteristics under projected growth. Dependency analysis covering external services, oracles, and infrastructure providers. Upgrade mechanisms and their governance implications.

**Domain 2: Code Quality and Technical Debt.** Static analysis results. Test coverage and test quality---not merely coverage percentage but whether tests exercise meaningful scenarios. Technical debt inventory: is debt tracked and being addressed? Deployment practices: frequency, automation, rollback capabilities.

**Domain 3: Security.** For Web3: smart contract audit history, formal verification, bug bounty maturity. For AI: model safety assessments, adversarial robustness, data privacy compliance. Infrastructure security: access controls, secret management, monitoring. Incident response history.

**Domain 4: Team and Capability.** Technical leadership depth and domain experience. Team composition relative to challenges ahead. Open-source contributions as capability signals. Knowledge concentration risk: is critical knowledge held by a single individual?

**Domain 5: Proprietary Advantage.** Uniqueness of approach relative to alternatives. Data advantages: proprietary datasets, feedback loops, network effects. Switching costs created by the architecture. Time-to-replicate estimate for a well-funded competitor.

### Red Flags That Should Halt Investment

Experienced technical due diligence practitioners have identified patterns that consistently predict problems. The presence of any single red flag does not necessarily disqualify an investment, but the accumulation of several should prompt serious reconsideration.

**Web3-Specific Red Flags:**
- Smart contracts never externally audited
- Upgrade mechanisms allowing a single key holder to modify contract logic without time locks
- Token contracts with hidden mint functions or unrestricted admin privileges
- Claims of "decentralization" contradicted by centralized key management
- Forked code with minimal modifications presented as novel technology

**AI-Specific Red Flags:**
- Inability to demonstrate model performance on held-out evaluation sets
- Training data provenance that is unclear or legally encumbered
- Claims of "proprietary AI" consisting primarily of prompt engineering atop commercial APIs
- No documented process for monitoring model drift in production

**Universal Red Flags:**
- CTO departure within 12 months without clear succession
- Version control history showing inactivity followed by large commits
- Discrepancy between marketing claims and actual technical capabilities
- Resistance to providing code access or facilitating technical deep dives

### Case Study: What Due Diligence Missed at FTX

The collapse of FTX in November 2022 represents perhaps the most consequential failure of technical due diligence in the history of technology investing. FTX raised approximately $1.8 billion from investors including Sequoia Capital, Paradigm, Tiger Global, and the Ontario Teachers' Pension Plan, among others. Many of these investors were among the most sophisticated in the world, with extensive experience evaluating technology companies.

The post-collapse analysis revealed technical deficiencies that a rigorous due diligence process should have identified. FTX operated without a dedicated security team for much of its existence. The exchange's internal accounting systems were so rudimentary that basic reconciliation of customer funds was not reliably possible. There was no independent board oversight of technology decisions or risk management. Alameda Research, the affiliated trading firm, had privileged access to FTX systems through what has been described in legal proceedings as a backdoor in the exchange's codebase---allowing exemption from the automated liquidation protocols that applied to all other users.

Several factors contributed to the failure of due diligence. First, the speed and competitive dynamics of the 2021 funding environment pressured investors to move quickly, compressing or eliminating technical review processes. Second, the opacity of a centralized exchange's internal systems made external technical assessment inherently more difficult than evaluating an open-source protocol. Third, and perhaps most critically, the social proof created by prior investors' participation substituted for independent evaluation---later investors relied on the assumption that earlier investors had conducted thorough due diligence.

The lessons are pointed. Technical due diligence cannot be delegated to other investors, regardless of their reputation. Centralized systems require more scrutiny, not less, precisely because their internals are not publicly visible. The absence of standard practices---independent boards, external audits, segregated customer funds---should be treated as disqualifying rather than as an acceptable feature of a fast-moving startup. And perhaps most importantly, the charisma and market narrative surrounding a founder should never substitute for independent verification of technical claims. Every major investor in FTX had the resources and expertise to conduct thorough technical due diligence. The failure was not one of capability but of process and discipline.

## 4. Smart Contract Audits and Security Assessments

### The Audit Ecosystem

Smart contract auditing has matured from an ad hoc practice into a structured industry with specialized firms, standardized methodologies, and a growing body of precedent. Understanding this ecosystem is essential for both founders commissioning audits and investors evaluating their results.

**Major Audit Firms and Their Specializations:**
- Trail of Bits: known for deep technical research, formal methods, and custom tooling development; particularly strong on novel cryptographic implementations
- OpenZeppelin: extensive experience with EVM-based contracts, maintainers of widely-used standard contract libraries, strong reputation in DeFi auditing
- Certora: specializes in formal verification, providing mathematical proofs of contract properties rather than solely manual review
- Consensys Diligence: broad experience across the Ethereum ecosystem with both manual and automated approaches
- Halborn: strong in operational security assessments that extend beyond smart contracts to encompass infrastructure and key management

**What a Quality Audit Includes:** Manual line-by-line code review by experienced auditors. Automated analysis using tools such as Slither, Mythril, or Echidna. Economic attack modeling. Access control analysis. Integration testing with external protocols and oracles. A detailed report classifying findings by severity (Critical, High, Medium, Low, Informational) with remediation recommendations.

**What an Audit Does Not Guarantee:** Freedom from all vulnerabilities---audits are bounded by time, scope, and auditor knowledge. Protection against post-audit changes, operational security failures, economic model flaws, or governance attacks.

### Evaluating Audit Quality

Not all audits are created equal, and the ability to distinguish a rigorous audit from a superficial one is a critical due diligence skill.

**Signs of a Thorough Audit:** Multiple auditors reviewed the codebase independently. The scope explicitly defines inclusions and exclusions. Findings include proof-of-concept exploits, not merely abstract descriptions. The report addresses economic incentive models. Follow-up verification confirms remediation.

**Signs of an Inadequate Audit:** Extremely short engagement timeline (less than two weeks for a complex protocol). Only Low or Informational findings, suggesting insufficient depth. No discussion of economic attack vectors. The firm has no verifiable track record. The audited codebase has since been substantially modified without re-audit.

### Case Study: The Audit That Prevented Catastrophe at Compound

In 2020, the DeFi lending protocol Compound engaged OpenZeppelin to audit a significant upgrade to its governance and token distribution system---the introduction of COMP token distribution to protocol users. The audit identified several critical issues, including a vulnerability in the proposal execution mechanism that could have allowed a carefully crafted governance proposal to drain protocol funds. The finding was classified as Critical severity, and the Compound team delayed the launch by several weeks to implement and verify the fix.

The significance of this finding becomes apparent when contextualized by subsequent events in DeFi. Governance attacks---where malicious actors acquire sufficient voting power to pass proposals that extract value from a protocol---became a recurring theme in 2021 and 2022. Beanstalk suffered a $182 million governance attack in April 2022 when an attacker used a flash loan to acquire enough voting power to pass a malicious proposal. Had the vulnerability identified in the Compound audit gone unaddressed, a similar attack vector would have been available against one of the largest protocols in DeFi, potentially affecting billions of dollars in user deposits.

The Compound case illustrates several principles of effective audit practice. First, audits are most valuable when conducted before launch rather than retroactively---the cost of delaying a launch by weeks is trivial compared to the cost of a major exploit. Second, the willingness to act on audit findings, even when doing so disrupts timelines, is a critical indicator of organizational maturity. Third, the audit process itself often serves an educational function, deepening the development team's understanding of their own system's attack surface and improving the quality of subsequent development. Investors evaluating a protocol's security posture should look not only at whether audits were conducted but at whether findings were addressed promptly and whether the process visibly improved the team's security practices over time.

## 5. AI Model Evaluation: Benchmarks, Data, and Moats

### The Challenge of Evaluating AI Companies

AI companies present a distinct set of due diligence challenges. Unlike smart contracts, where the code is the product and can be directly inspected, AI models are opaque artifacts whose behavior emerges from the interaction between architecture, training data, and optimization procedures. Evaluating an AI company requires assessing not only the model's current performance but the sustainability and defensibility of the processes that produced it.

**Benchmark Assessment:**
- Performance on established benchmarks relevant to the application domain (MMLU, HumanEval, HELM for language models; ImageNet, COCO for vision; domain-specific benchmarks for specialized applications)
- Performance on held-out evaluation sets that the model has not been trained on
- Comparison to publicly available baselines: does the model meaningfully outperform open-source alternatives?
- Robustness testing: how does performance degrade with adversarial inputs, distribution shift, or edge cases?
- Latency and cost metrics under production conditions, not merely accuracy on static benchmarks

**Data Quality Assessment:**
- Provenance and legal status of training data: are there licensing risks or potential copyright claims?
- Data cleaning and annotation processes: what quality controls are applied?
- Representativeness of training data relative to the target deployment context
- Ongoing data collection mechanisms: does the company have sustainable access to high-quality data?
- Privacy compliance: GDPR, CCPA, and sector-specific data regulations

**Moat Assessment:**
- Proprietary data advantages that would be difficult or expensive for competitors to replicate
- Feedback loops where deployment generates data that improves the model
- Domain-specific fine-tuning or RLHF that creates specialization competitors lack
- Infrastructure optimizations (custom inference engines, model compression techniques) that reduce cost
- Relationships with data providers or domain experts that are not easily reproduced

### Case Study: How Cohere's Enterprise AI Evaluation Process Set Industry Standards

The Canadian AI company Cohere, founded in 2019 by former Google researchers including Aidan Gomrat, developed what became a widely-referenced approach to enterprise AI model evaluation during its Series C process in 2023. Rather than relying solely on standard academic benchmarks, Cohere worked with prospective enterprise customers to define evaluation suites that reflected actual production use cases.

For each target vertical---legal, financial services, healthcare---Cohere constructed domain-specific evaluation sets in collaboration with subject matter experts. A legal document analysis evaluation, for instance, included not only accuracy metrics on contract clause identification but measurements of hallucination rates on domain-specific terminology, consistency across document formats, and performance degradation as document length increased. For financial services applications, the evaluation incorporated regulatory compliance checking, numerical accuracy in financial calculations, and appropriate handling of uncertainty in market predictions.

Cohere documented and presented this evaluation methodology as part of its fundraising materials, enabling investors to assess not merely the model's current performance but the sophistication and rigor of the evaluation process itself. Investors could examine whether the benchmarks were genuinely challenging, whether the evaluation methodology was reproducible, and whether the results were statistically significant rather than anecdotal.

This approach addressed a fundamental asymmetry in AI investing: investors typically lack the domain expertise to independently evaluate model quality. By providing a transparent evaluation framework, Cohere enabled investors to evaluate the process rather than solely the outputs---a distinction that proved decisive in securing favorable terms. The company raised $270 million in its Series C at a $2.2 billion valuation, with multiple investors citing the transparency and rigor of the technical evaluation as a differentiating factor. Cohere's approach also established a precedent: increasingly, sophisticated AI investors expect companies to present not only benchmark results but the methodology behind those results, including failure case analysis and honest documentation of model limitations.

## 6. Code Quality Metrics and Technical Debt Assessment

While code quality cannot be fully captured by metrics alone, quantitative indicators provide useful signals when interpreted in context. Due diligence should combine automated metrics with qualitative review.

**Key Metrics to Examine:**
- Static analysis: cyclomatic complexity, code duplication (above 5 percent suggests insufficient abstraction), dependency freshness, and dead code percentage
- DORA framework metrics: deployment frequency, lead time for changes, mean time to recovery, and change failure rate---these four metrics correlate strongly with overall organizational performance
- Technical debt tracking: is debt explicitly catalogued, is engineering time allocated to reduction, and are constraining architectural decisions being addressed?

Raw metrics without context are misleading. A smart contract with 95 percent test coverage may still contain critical vulnerabilities if the tests do not exercise adversarial scenarios. Investors should request codebase access (under NDA if necessary) and allocate time for hands-on review by a qualified assessor who examines not only the current state but the trajectory: is quality improving or degrading over time?

## 7. Infrastructure Scalability Evaluation

Scalability evaluation examines whether the technical infrastructure can support projected growth without requiring a fundamental redesign. For Web3 and AI companies, constraints often emerge in unexpected places.

**Web3 Scalability Considerations:**
- Transaction throughput under load: has the protocol been stress-tested?
- State growth management and cross-chain interoperability security
- Oracle dependency scaling: do feeds maintain accuracy under high-volume conditions?

**AI Scalability Considerations:**
- Inference cost trajectory: does per-query cost decrease with scale?
- Model serving infrastructure: load balancing, failover, and geographic distribution
- Data pipeline and retraining cadence: can the system keep pace with growth?

**Infrastructure Dependencies:**
- Concentration risk with a single cloud provider
- Cost optimization through reserved instances, spot pricing, or custom hardware
- Disaster recovery: is there a tested plan for infrastructure failure?

Claims about scalability should be substantiated by evidence. Investors should request load testing results, architecture diagrams, and documentation of peak load performance. For early-stage companies, the evaluation should focus on whether the architecture is designed to scale---examining database choices, caching strategies, and the separation of concerns that enables horizontal scaling.

## 8. Team Technical Capability Assessment

### Evaluating the Technical Team

The quality of the technical team is arguably the single most important factor in technical due diligence. Technology can be rebuilt, architectures can be refactored, and technical debt can be paid down---but only if the team has the capability to do so.

**Individual Assessment:** Relevant domain experience---has the team built comparable systems? Publication record and conference presentations. Open-source contributions demonstrating quality, consistency, and community engagement. Technical leadership shown through architectural vision and decision-making under uncertainty.

**Team Composition:** Coverage of critical domains (for Web3: smart contracts, cryptography, security; for AI: ML engineering, data engineering, MLOps, safety). Depth versus breadth balance. Retention patterns and stability.

**Open-Source Contributions as Signal:** A team's open-source work provides a uniquely transparent signal. Unlike resumes, it is publicly verifiable and demonstrates actual coding ability and collaborative skills. Investors should examine contributions to relevant high-profile projects, quality of code reviews, responsiveness to issues, and whether the company contributes upstream to its dependencies.

### Knowledge Concentration Risk

One of the most critical and frequently overlooked risks in early-stage technical organizations is knowledge concentration---where critical understanding of the system's architecture, deployment, or operational procedures resides in a single individual. This creates a single point of failure that can be catastrophic if that individual departs, becomes unavailable, or is incapacitated.

Investors should probe for knowledge concentration by asking: if the CTO were unavailable for three months, could the team continue to operate and ship? If the answer is uncertain, that is a material risk that should be addressed.

## 9. Tokenomics Model Validation

### Technical Evaluation of Token Economics

For Web3 companies, the tokenomics model represents a critical intersection of technical implementation and economic design. Due diligence must evaluate both the theoretical soundness of the economic model and the fidelity of its implementation in code.

**Economic Model Validation:**
- Supply mechanics: are issuance, burning, and supply adjustment mechanisms implemented correctly?
- Incentive alignment: do the token incentives actually encourage the behaviors the protocol requires?
- Attack vector analysis: can the token economics be exploited through flash loans, wash trading, or governance manipulation?
- Simulation results: has the team modeled the token economy under stress scenarios (rapid growth, sudden contraction, adversarial conditions)?

**Implementation Verification:**
- Do the smart contracts implement the tokenomics as described in the documentation?
- Are there discrepancies between the whitepaper and the deployed code?
- Are token distribution schedules enforced on-chain or managed by centralized systems?
- Vesting contracts: are they immutable, or can the team modify vesting terms?

**Market Dynamics Assessment:**
- Liquidity concentration: is token liquidity dependent on a small number of market makers?
- Unlock schedule impact: when do large token unlocks occur, and what sell pressure might they create?
- Circular revenue: is protocol revenue genuinely organic, or is it substantially derived from token incentive programs?

## 10. The Role of Third-Party Auditors

### Engaging and Evaluating Auditors

Third-party auditors serve as an essential component of the due diligence ecosystem, but their role must be properly understood. An audit is not a guarantee of security---it is an expert opinion bounded by scope, time, and methodology.

**Selecting the Right Auditor:** Match auditor expertise to your technology (EVM contracts, Rust/Solana, zero-knowledge circuits). Request references from comparable projects. Understand methodology: formal verification, fuzz testing, manual review, or a combination. Evaluate resource allocation and confirm professional liability insurance.

**Maximizing Audit Value:** Provide comprehensive documentation, not just code. Brief auditors on intended behavior and known risks before engagement. Engage early in the development cycle. Conduct re-audits after significant changes.

**The Emerging Role of Formal Verification:** Formal verification---mathematical proof that code conforms to a specification---has moved from academic curiosity to practical tool. Certora and Runtime Verification have developed tooling for meaningful verification of smart contract properties. While it cannot prove the absence of all bugs (the specification itself may be incomplete), it provides assurance that manual review alone cannot match for critical invariants such as "user balances can never become negative."

## 11. A Non-Western Perspective: Technical Due Diligence in Southeast Asia's Web3 Ecosystem

### Case Study: Sky Mavis and the Ronin Bridge---Lessons from the Philippines

The March 2022 Ronin bridge hack, which resulted in the theft of approximately $625 million in ETH and USDC, provides a compelling case study in technical due diligence within a non-Western context. Sky Mavis, the Vietnamese-founded company behind Axie Infinity, had built one of the most successful Web3 applications in the world, with particular adoption across the Philippines and Southeast Asia.

The Ronin bridge operated with only nine validator nodes, of which five were required to authorize transactions. Sky Mavis controlled four of these validators directly and had been temporarily granted control of a fifth by the Axie DAO to handle high transaction volumes---an arrangement that was never revoked. When an attacker compromised Sky Mavis's systems, they gained control of five validators and could authorize arbitrary withdrawals.

The due diligence implications are significant and extend beyond the technical specifics. First, the bridge's validator structure represented a centralization risk that would have been identifiable through standard technical due diligence. A review of the validator set---who controls each node, what the quorum requirements are, and whether any single entity has effective control---is a straightforward assessment that any qualified technical reviewer could perform. Second, the temporary governance decision to grant Sky Mavis additional validator control was never reversed, illustrating how operational decisions can silently erode security assumptions. Technical due diligence must evaluate not only the system as designed but the system as actually operated.

The broader context matters as well. The Ronin bridge served millions of users in developing economies, many of whom were earning meaningful income through the Axie Infinity play-to-earn model. The bridge's security architecture had direct consequences for the livelihoods of real people. This raises a question that technical due diligence frameworks must grapple with: should the standard of care be elevated when the user base is disproportionately composed of individuals who lack the financial resilience to absorb losses? The answer, from both ethical and practical perspectives, is yes---the reputational and regulatory consequences of failures affecting vulnerable populations are amplified, and due diligence processes should account for this. Sky Mavis ultimately raised $150 million to reimburse affected users and rebuilt the bridge with a significantly expanded validator set and improved security architecture. The lesson for investors and founders alike is that bridge security and cross-chain infrastructure deserve the highest level of scrutiny in any Web3 due diligence process, particularly when the system serves as critical infrastructure for a large user base.

## 12. Post-Investment Technical Governance

Technical due diligence does not end when the investment is made. The post-investment period requires governance structures that maintain technical quality and provide investors with ongoing visibility.

**Technical Advisory Boards:** Establish an independent advisory board that meets quarterly, has codebase access, and provides candid assessments shared with investors. Board members should be domain experts with no conflicts of interest.

**Ongoing Security Practices:** Continue external audits after significant code changes. Maintain and expand bug bounty programs. Implement real-time monitoring for anomalous behavior. Conduct periodic tabletop exercises and maintain tested incident response playbooks.

**Technical Reporting:** Include technical metrics---deployment frequency, test coverage, incident count, audit findings, and technical debt trajectory---in regular investor updates. Flag significant risks or architectural decisions that may affect the company's trajectory.

**Web3 Governance Mechanisms:** Establish multi-signature requirements with time locks for critical contract upgrades. Implement on-chain governance with appropriate quorum requirements. Create transparent emergency processes (circuit breakers, pause mechanisms) and ensure governance power evolves toward decentralization over time.

## 13. Implementation Guide: The Dual-Sided Due Diligence Checklist

### For Founders: Preparing Your Company

**Phase 1: Foundation (3-6 Months Before Fundraising).** Commission at least one external security audit. Establish code review processes with consistent enforcement. Document all architectural decisions through ADRs. Implement automated testing with coverage reporting. Create system architecture diagrams and establish vulnerability disclosure processes.

**Phase 2: Documentation (2-3 Months Before Fundraising).** Compile a technical dossier: audit reports, architecture documentation, team credentials, and benchmark results. Prepare a clear technical narrative addressing architecture choices, moat, and risk awareness. Document known technical debt and the remediation plan.

**Phase 3: Readiness (1 Month Before Fundraising).** Conduct an internal mock due diligence with a trusted external advisor. Address critical findings. Prepare a secure data room with organized materials. Brief the technical team on investor conversations and ensure consistent articulation of the technical vision.

### For Investors: Conducting the Review

**Stage 1: Initial Screening (1-2 Days).** Review publicly available information---GitHub repositories, audit reports, technical blogs. Assess team credentials and identify obvious red flags.

**Stage 2: Deep Technical Review (1-3 Weeks).** Request codebase access under NDA. Evaluate architecture, code quality, security, and team capability using the five-domain framework in Section 3. Conduct technical interviews with the CTO and lead engineers. Review audit reports and remediation.

**Stage 3: Risk Assessment (3-5 Days).** Compile findings into a structured risk assessment classified by severity and likelihood. Identify acceptable risks, risks requiring mitigation as investment conditions, and disqualifying risks.

**Stage 4: Post-Investment Monitoring (Ongoing).** Establish regular technical reporting. Define trigger events for escalated review. Maintain relationships with the technical team for early identification of emerging risks.

---

## In This Chapter

- Technical due diligence in Web3 and AI is fundamentally more consequential than in traditional software ventures because vulnerabilities can result in immediate, irreversible financial losses or catastrophic regulatory exposure.
- Founders who build diligence-ready organizations as a default practice---rather than preparing only before fundraising---gain significant advantages in both investor confidence and actual technical quality.
- The FTX collapse demonstrated that even the most sophisticated investors can fail at technical due diligence when competitive dynamics compress review timelines and social proof substitutes for independent evaluation.
- Smart contract audits are necessary but not sufficient: they represent point-in-time assessments and must be complemented by ongoing security practices including bug bounties, monitoring, and periodic re-audits.
- AI model evaluation requires domain-specific benchmarks, transparent methodology, and honest documentation of limitations---generic benchmarks alone are inadequate for assessing production readiness.
- Technical team quality is the single most important factor in due diligence; open-source contributions provide uniquely transparent signals of capability.
- Tokenomics validation must verify both the theoretical soundness of the economic model and the fidelity of its implementation in code.
- Post-investment technical governance---including advisory boards, ongoing audits, and regular technical reporting---is essential for maintaining the quality that due diligence initially validated.

## Checklist

- [ ] Commission at least one external security audit from a reputable firm before approaching investors
- [ ] Document all architectural decisions with rationale through Architecture Decision Records
- [ ] Maintain test coverage above 80 percent for critical paths with automated CI/CD enforcement
- [ ] Create a technical dossier including audit reports, architecture diagrams, team credentials, and benchmark results
- [ ] Conduct a mock due diligence exercise with a trusted external technical advisor
- [ ] Review all smart contracts for admin backdoors, unrestricted mint functions, and centralized upgrade authority
- [ ] For AI companies: prepare domain-specific evaluation suites with reproducible methodology and held-out test sets
- [ ] Assess knowledge concentration risk and document plans for knowledge distribution across the team
- [ ] Verify tokenomics implementation matches whitepaper specification through code review
- [ ] Establish post-investment technical governance structure including advisory board and reporting cadence
- [ ] Implement vulnerability disclosure process and incident response playbooks
- [ ] Evaluate all cross-chain bridges and oracle dependencies for centralization risks and failure modes

## Exercises

- **Exercise 1: Red Flag Identification.** Select three Web3 or AI projects that have publicly available GitHub repositories. For each, spend 30 minutes examining the repository and identify as many red flags from the framework in Section 3 as you can find. Compare your findings against any publicly known issues with these projects. What did you catch, and what did you miss?

- **Exercise 2: Mock Technical Due Diligence.** If you are a founder, invite a technically qualified advisor to conduct a two-hour mock due diligence session on your company. Provide them with codebase access, documentation, and audit reports in advance. Ask them to prepare a written assessment using the five-domain framework (Architecture, Code Quality, Security, Team, Proprietary Advantage). Use their findings to identify and prioritize areas for improvement.

- **Exercise 3: Audit Report Analysis.** Obtain three publicly available smart contract audit reports (many are published by protocols or available on audit firm websites). For each report, evaluate: (a) the scope of the audit, (b) the severity distribution of findings, (c) whether the protocol addressed the findings, and (d) whether the audit methodology was appropriate for the complexity of the protocol. Write a one-page assessment of each audit's quality.

- **Exercise 4: AI Model Evaluation Design.** Design a technical due diligence evaluation framework for an AI company in a domain you are familiar with. Define: (a) the specific benchmarks you would require, (b) the held-out evaluation methodology, (c) the robustness tests you would conduct, (d) the data provenance questions you would ask, and (e) the moat assessment criteria. Compare your framework to the approach described in the Cohere case study.

- **Exercise 5: Post-Investment Governance Design.** Design a post-investment technical governance framework for either a Web3 protocol or an AI company. Specify: the composition of the technical advisory board, the reporting metrics and cadence, the trigger events for escalated review, and the governance mechanisms for critical technical decisions. Present your framework to a peer and incorporate their feedback.

## Sources

1. Trail of Bits (2024). *"Building Secure Smart Contracts: Security Guidance and Best Practices."* Trail of Bits Blog and Documentation.

2. OpenZeppelin (2024). *"Security Audits: Methodology and Approach."* OpenZeppelin Documentation.

3. Certora (2024). *"Formal Verification for DeFi: Principles and Practice."* Certora Technical Documentation.

4. Lewis, M. (2024). *Going Infinite: The Rise and Fall of a New Tycoon.* W.W. Norton and Company.

5. Chainalysis (2023). *"The 2023 Crypto Crime Report: Cross-Chain Bridge Exploits and DeFi Hacks."* Chainalysis Annual Report.

6. Forsyth, N., Puppala, S., and Perez, D. (2023). "Empirical Analysis of Smart Contract Audit Effectiveness." *IEEE Symposium on Security and Privacy Workshops*, 2023.

7. Cohere (2023). *"Enterprise AI Evaluation: Building Trust Through Transparent Benchmarking."* Cohere Technical Blog.

8. DORA Team, Google Cloud (2024). *"Accelerate State of DevOps Report 2024."* Google Cloud and DevOps Research and Assessment.

9. Rekt News (2024). *"Leaderboard: Largest DeFi Exploits by Value Lost."* rekt.news. Accessed March 2026.

10. Electric Capital (2024). *"Developer Report 2024: Open Source Contributions and Developer Activity in Crypto."* Electric Capital Annual Report.

11. Elliptic (2023). *"Cross-Chain Crime: Analyzing Vulnerability Patterns in Blockchain Bridges."* Elliptic Research Report.

12. Stanford HAI (2024). *"AI Index Report 2024: Model Evaluation, Safety, and Governance."* Stanford Institute for Human-Centered AI.

13. Immunefi (2024). *"Crypto Losses in 2023: Annual Report on Hacks, Scams, and Exploits."* Immunefi Annual Report.

14. U.S. Securities and Exchange Commission (2023). *"SEC Charges Samuel Bankman-Fried with Defrauding Investors."* SEC Litigation Release, November 2023.

15. Sky Mavis (2022). *"Ronin Bridge Post-Mortem: What Happened and What We Are Doing About It."* Axie Infinity Blog, March 2022.
