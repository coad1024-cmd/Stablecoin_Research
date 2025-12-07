# **SoK: Blockchain Governance**



Aggelos Kiayias
University of Edinburgh, Input Output
Edinburgh, United Kingdom
aggelos.kiayias@ed.ac.uk


**ABSTRACT**


Blockchain systems come with a promise of decentralization that,
more often than not, stumbles on a roadblock when key decisions
about modifying the software codebase need to be made. In a setting
where “code-is-law,” modifying the code can be a controversial process, frustrating to system stakeholders, and, most crucially, highly
disruptive for the underlying systems. This is attested by the fact
that both of the two major cryptocurrencies, Bitcoin and Ethereum,
have undergone “hard forks” that resulted in the creation of alternative systems which divided engineering teams, computational
resources, and duplicated digital assets creating confusion for the
wider community and opportunities for fraudulent activities. The
above events, and numerous other similar ones, underscore the importance of Blockchain governance, namely the set of processes that
blockchain platforms utilize in order to perform decision-making
and converge to a widely accepted direction for the system to evolve.
While a rich topic of study in other areas, including social choice
theory and electronic voting for public office elections, governance

- f blockchain platforms is lacking a well established set of meth
- ds and practices that are adopted industry wide. Instead, different
systems adopt approaches of a variable level of sophistication and
degree of integration within the platform and its functionality. This
makes the topic of blockchain governance a fertile domain for a
thorough systematization that we undertake in this work.
Our methodology starts by distilling a comprehensive array of
properties for sound governance systems drawn from academic
sources as well as grey literature of election systems and blockchain
white papers. These are divided into seven categories, suffrage,
Pareto efficiency, confidentiality, verifiability, accountability, sustainability and liveness that capture the whole spectrum of desiderata of governance systems. We interpret these properties in the
context of blockchain platforms and proceed to classify ten blockchain systems whose governance processes are sufficiently well
documented in system white papers, or it can be inferred by publicly available information and software. While all the identified
properties are satisfied, even partially, by at least one system, we

- bserve that there exists no system that satisfies most properties.
Our work lays out a common foundation for assessing governance
processes in blockchain systems and while it highlights shortcomings and deficiencies in currently deployed systems, it can also be
a catalyst for improving these processes to the highest possible


[This work is licensed under a Creative Commons Attribution International 4.0 License.](https://creativecommons.org/licenses/by/4.0/)


_AFT_ _’22,_ _September_ _19–21,_ _2022,_ _Cambridge,_ _MA,_ _USA_
© 2022 Copyright held by the - wner/author(s).
ACM ISBN 978-1-4503-9861-9/22/09.
[https://doi.org/10.1145/3558535.3559794](https://doi.org/10.1145/3558535.3559794)



Philip Lazos
Input Output
London, United Kingdom
philip.lazos@iohk.io


standard with appropriate trade-offs, something direly needed for
blockchain platforms to operate effectively in the long term.


**ACM Reference Format:**

Aggelos Kiayias and Philip Lazos. 2022. SoK: Blockchain Governance. In _4th_
_ACM Conference on Advances in Financial Technologies (AFT ’22), September_
_19–21, 2022, Cambridge, MA, USA._ ACM, New York, NY, USA, 13 pages.
[https://doi.org/10.1145/3558535.3559794](https://doi.org/10.1145/3558535.3559794)


**1** **INTRODUCTION**


Following the founding of Bitcoin [57] in 2009, cryptocurrencies and

- ther blockchain platforms have tremendously risen in popularity.
Unlike centralised organisations, which are governed by a select
few, blockchain platforms operate in a decentralised fashion by
the different actors in these platforms. The decentralised nature

- f blockchains has been essential to their appeal; however, it has
also introduced new challenges. Blockchain platforms, like other

- rganisations, try to adapt and adjust to their stakeholders’ needs
and preferences. With different actors present whose preferences
might not always align, governance problems arise and the risk of
division between their community members increases.
Different governing mechanisms exist, depending on the platform. Off-chain governance is the most centralised of such mechanisms with the core developers or the most trusted contributors
making most of the decisions. On-chain governance is achieved via

- n-chain voting mechanisms, which can be more transparent and
inclusive than off-chain governance. In both of these mechanisms,
community division can take place when a backward-incompatible
update is adopted, where some stakeholders choose to stay on the

- riginal chain and others choose to upgrade to the updated chain,
dividing the community into two. Alternatively, two or more competing updates may be proposed dividing the community about
their potential merits. Eventually, consensus can fail and different
segments of the community adopt the update that they believe to
be the most beneficial.

In the most general sense, such deviations are known as hard
forks and numerous examples of them have been observed in popular cryptocurrencies. Two notable examples are the split of the
Ethereum chain to Etheurem and Ethereum Classic due to the the

DAO debacle [1] and the split of the Bitcoin system into Bitcoin
and Bitcoin Cash over the debate around block size and the SegWit
upgrade. Such divisions can fragment the community and its resources, and as a result reduce the overall value of the platform as
well as its security. The latter consideration can be quite tangible
as the reduced number of resources supporting a fork can lead
to attacks. Such attacks are referred to as 51% attacks and have

- ccurred on a number of occasions, e.g., see the case of Ethereum
Classic [2] for a notable such instance.



61


AFT ’22, September 19–21, 2022, Cambridge, MA, USA


The above issues highlight the importance of sound blockchain
governance, the ability of a blockchain platform community members to express their will effectively regarding the future evolution

- f the platform as well as the best possible utilization of its resources.
So this brings forth the question what characterizes proper governance in blockchain systems? This fundamental question motivates
the systematization effort we undertake in this paper.
Our methodology is first to derive a set of properties, that are
drawn from general governance principles and election theory
and then interpret them to the blockchain governance setting. We
use a variety of sources to ensure the comprehensiveness of our
property list that include the Council of Europe technical standards for e-voting [3], the Federal Election Commission’s Voting
Systems Standards [4], but also blockchain specific ones such as

[5, 6, 56]. Given the set of properties, we then evaluate a wide array

- f blockchain platforms against those properties revealing each
platform’s unique strengths and weaknesses.
We distill seven fundamental properties for blockchain governance, which capture different aspects of important requirements
for governance. The first property deals with participation eligibility.
Decision making systems can produce legitimate outcomes provided they are inclusive, a property we capture by different aspects

- f _Suffrage_ adapted to the blockchain setting. Suffrage determines
a set of “decision-makers” who are a subset of the community of a
blockchain project. The second property has to do with the _Confi-_
_dentiality_ - f the decision-makers’ inputs; it further specializes to Privacy, which asks for maintaining the input private while Coercion
Resistance asks for the input to be free of any external influences.
The third property, _Verifiability_, asks for decision-makers to be able
to verify their input has been taken into account and the output is
correctly computed. These last two properties are in a sense “classical” security properties. Next we move to two properties that have
to do with the incentives of the decision-makers. _Accountability_
asks for decision-makers to be held accountable for the input they
provide to the system, while _Sustainability_ asks whether appropriate incentives are provided for the system to evolve constructively
and to the decision-makers for providing meaningful input. We
then move to a social choice consideration. _Pareto efficiency_ asks
that, given all decision-makers’ preferences, the outcome of the
governance process cannot be strictly improved vis-à-vis these preferences. Finally, the crucial ability of the system to produce outputs
expediently is captured by _Liveness._
Armed with the above comprehensive list of governance properties we investigate a number of popular blockchain platforms
which provide some sort of governance functionality and we detail
the way they satisfy (or fail to satisfy) each of the given properties.
Our results dictate that while each of the properties is considered
in the context of at least one system, there exists no platform that
satisfies most of the properties.


**1.1** **Related Work**


As of the time of writing, there is yet to be a formal or rigorous
coverage of good blockchain governance properties. However, the
topic of blockchain governance has received coverage in multiple
disciplines. Given their diversity, additional related work is also
presented in context within each subsection of Section 2, where



each governance property is defined. Pelt et al. [59] adapt the definition of OSS (open-source software) governance to blockchain
governance; they then go on to derive six dimensions and three
layers of blockchain governance from the literature to build a framework, which can be used as a starting point for discussion in new
blockchain projects. Similarily Beck et al. [30] derive three key
dimensions of blockchain governance to define an IT governance
definition. De Filippi and McMullen [42] investigate the social and
technical governance of Bitcoin, making a distinction between two
coordination mechanisms: governance by the infrastructure (via the
protocol) and governance of the infrastructure (by the community

- f developers and other stakeholders). Corporate governance has
been drawn from in the literature to examine the governance of public blockchains. The work done by Hsieh et al. [49] and Allen and
Berg [23] are such examples, where the authors of the latter work
derive a definition of blockchain governance and make a distinction between endogenous and exogenous governance. Given the
variety of actors and strategies in the decision-making processes in
blockchain platforms, Khan et al. [51] view blockchain governance
from the lens of IT governance and then analyse decision-making
processes in the form of voting on a new blockchain improvement
proposal, by using Nash equilibria to predict optimal governance
strategies. Certain forms of blockchain governance, like traditional
forms of governance, have the short-coming of participants not
able to change their vote between two consecutive elections or
votes. Venugopalan and Homoliak [68] address this shortcoming,
among others, by introducing an always-on-voting (AoV): a repetitive blockchain-based voting framework that allows participants to
continuously vote and change elected candidates or policies with
- ut having to wait for the next election. More specific analysis on
certain aspects of blockchain decision-making processes also exist
in the literature (e.g. Gersbach et al. [44] where the authors analyse
delegated voting and conclude caution should be exercised when
implementing such mechanisms).


**2** **BLOCKCHAIN GOVERNANCE PROPERTIES**


One of the main contributions of our work is systematizing the
properties pertinent to blockchain governance systems. We would
like to stress that there is no _single set_ that optimally captures every
aspect. There are trade-offs between satisfying some properties to
a high degree and others to a lesser degree. In addition, many current implementations do not have rigorously defined governance
mechanisms for every use case and usually contain a mixture of
formal on-chain features as well as informal off-chain ones. This

is almost inevitable, as different blockchains are built for specific
purposes and not all decision-making processes can be sufficiently
captured by a smart contract or special purpose protocol logic. Others might still be centralized or transitioning to full decentralization.
Irrespective of this, our property systematization focuses on _first_
_principles_ and is meaningful across the board, independently of
the underlying set of mechanisms that are set in place to facilitate
decision-making in each blockchain platform.
We can categorize the properties into four broad classes pictorially shown in Figure 1. The first class contains properties about
the _voting system_ that is used for decision-making. It will touch
the issues of who is eligible to participate and what is the process



62


SoK: Blockchain Governance AFT ’22, September 19–21, 2022, Cambridge, MA, USA



that combines the inputs provided. The voting system enables us to
argue about the governance process in an ideal, philosophical sense;
questions such as who has the right to vote are relevant here. The
remaining three classes deal with the way an ideal voting system
can be implemented and touch three important domains: _security_
which deals with cryptographic and cyber-security aspects, _incen-_
_tives_ which deals with game-theoretic and economics aspects, and
_timeliness_ which deals with issues of time and expediency. Within,
the keywords _Deliberation_ and _Execution_ are greyed-out. These are
not the focus of our systematization. The reasoning behind this will
be explained below. Failures in the properties of these classes can
have important repercussions for the legitimacy of the governance
process. Even though the voting system might be acceptable in a
‘Platonic’ ideal sense, failures in the remaining properties can suggest that certain community members are disenfranchised because
it is harder for them to participate, or they cannot express their will
freely or even that they have no ability to properly form an opinion
due to lack of proper incentivization. It is also worth adding that
_usability_ permeates these three implementation related classes, but
it will be outside of scope of our systematization.


**Figure 1: The partition map of governance properties.**


An important aspect of our property systematization is that we
emphasize fundamental properties entirely decoupling them from
any specific techniques, algorithms or mechanisms that support
them. To illustrate the point, a simple example is the distinction
between the property of having privacy (or secrecy) and the cryptographic protocol techniques that may be used to achieve it. Another
example is quadratic voting, which is a technique where additional
votes can be ‘bought’ (using actual money, voting credit, etc.) but
the cost scales quadratically with the number of votes. Even though
it has received renewed interest in blockchain governance, particularly for participatory budgeting applications, [1] it should be clear
it is still just a _mechanism_, not a fundamental property per se; we
revisit it in some more detail when we discuss Suffrage below as it
is one of our basic properties that is most related.
Further to this point, whether a particular governance mechanism is on-chain, off-chain, uses a foundation etc. is a _mechanism_,
**not** a property. These inner workings will not be part of our classification explicitly, unless they affect some fundamental property.


[1Such as Gitcoin quadratic funding, https://gitcoin.co/blog/gitcoin-grants-quadratic-](https://gitcoin.co/blog/gitcoin-grants-quadratic-funding-for-the-world/)
[funding-for-the-world/](https://gitcoin.co/blog/gitcoin-grants-quadratic-funding-for-the-world/)



We want to stress that satisfying all properties to some higher or
lower degree, as permitted by their interaction, would not make a
blockchain governance system perfect. There are many blockchains
applications and each of them has different needs and use cases
that would require community involvement. Some properties might
be incompatible with each other. Our thesis though is that any
design would have to _consider_ how each property is addressed and
ensure that the the choices made are deliberate. As such, during the
evaluation of different governance systems we will make sure that
each property is judged _in context_, taking the goals of each system

into account.


_Timeliness: scope and limitations._ In describing the properties
(excluding, to an extent, _liveness_ ) we take a high-level, theoretical
approach, obviating the need to explain the underlying social and

- rganizational structures that power the governance systems which
exhibit them. This is intentional: by remaining abstract we can cover
a sufficiently large ‘space’ of governance system designs, without
sacrificing too much detail. Still, it is important to acknowledge
such structures as they are an integral part of governance. First,
it should be possible (and easy) for the users to _deliberate_ (often
done through github, Discord or public internet forum) in order
to converge on the topics that need to enter the decision-making
process. Second, the manner which the executive power is conferred
is critical. In some (simpler) cases it is possible to make execution
automated — while other times larger structures (such as a private
enterprise or non-profit foundation) can engage to implement the

- utcomes of the decision making process. As a takeaway, our focus
will be the study of governance process in between Deliberation
and Execution, assuming both of them are feasible.


**2.1** **Suffrage**


One of the first considerations of any governance system is determining who is granted _suffrage_, which is the right to participate
in decision making procedures. This can be distinguished in _active_
suffrage, the right to vote, and _passive_ suffrage, which is the right to
stand for election and become an elected representative. Suffrage,
an already a complicated and nuanced property, is even more so
when applied to blockchain systems.
In national or regional elections, it is often the case that the
voting mechanism implements a ‘one person, one vote’ rule. Different jurisdictions use different criteria in guaranteeing the right
to vote to individuals, but the bottom line is that one person can

- nly submit one vote. Although research is currently underway on
proof-of-personhood systems [66], which verify that accounts correspond to unique individuals, the ‘one person, one vote’ rule is not
applicable to most, if not any, current blockchain platforms. Instead,
we often see that a minimum amount of stake or hashing power
is required to guarantee a vote. We also see platforms where only
the founders or core developers are guaranteed a vote. In any case,
these are attempts to define and reconcile two groups of people:
the set of community-members _𝐶_ and decision-makers _𝐷_ .


Definition 1. _The community-members 𝐶_ _of a blockchain sys-_
_tem are people that have_ direct _interaction with it. This may be by_
_providing resources in service of its security or consensus protocol,_

_owning tokens, develop software etc._



63


AFT ’22, September 19–21, 2022, Cambridge, MA, USA


Definition 2. _The decision-makers 𝐷_ ⊆ _𝐶_ _of a blockchain system_
_are the people that participate in (any way) its governance._


Given these definitions, we establish the basic ways that community-members are granted voting rights in the blockchain space.
The voting rights should more accurately be called voting _weights_,
as it is very common to allocate a different number of votes across
all community-members.


Definition 3 (Type 1: Identity-Based Suffrage). _A blockchain_
_governance system satisfies this property if it guarantees decision-_
_making rights to participants who are able to prove their identities_
_such that the votes correspond to unique individual humans._


Contrary to the usual notion of community-membership, identity alone is not (so far) a robust enough connection between users
and blockchains. Also, there is no restriction against switching to
different blockchains or having direct interactions with many of
them. The following notions of suffrage are based on a more ‘quantifiable’ approach and typically assign voting power accordingly.


Definition 4 (Type 2: Token-Based Suffrage). _A blockchain_
_governance system satisfies this property if it guarantees decision-_
_making rights to participants who have certain tokens in the platform_

_or a minimum amount of tokens in the platform._


Definition 5 (Type 3: Mining-Based Suffrage). _A blockchain_
_governance system satisfies this property if it guarantees decision-_
_making rights to participants who have a certain amount of hashing_
_power in the platform (or other physical resource relevant to the_
_platform, e.g., disk storage)._


In the PoS setting, voting weight is often measured by an operator’s stake (or wealth). This can result in the following undesirable
situations: **(i)** participants who may be more enthusiastic about
the platform have lower voting weight than those who are less
enthusiastic about the platform, and **(ii)** participants who may have
contributed more to the platform may have lower voting weight
than those who contributed less. Methods like quadratic voting

[55] can help dampen the effects of stake-based voting weight (see
below for an explanation), but it does not address the root of the
problem: voting weight is ultimately based on wealth owned or
even managed (e.g., centralized cryptocurrency exchanges may
control a significant amount of stake that does not belong to them).
Similar issues exist in the PoW setting, where hashing power may
not proportionately reflect stakeholder contributions to the platform. Analysis in quantifying decentralisation [7] on blockchain
platforms, in terms of stake and hashing power, can provide insights
into resultant power concentrations.


Remark (Governance Tokens). _Often, tokens used to determine_
_suffrage can have more than one use (e.g., native currency of a proof-_

_of-stake system). However, particularly for the governance of smart_
_contract based protocols, specific_ governance _tokens can be used,_
_who have no other direct functionality or value (such as paying for_
_transaction fees or appearing as block rewards) other than enabling_
_participation. Especially when these tokens are transferable, special_
_care is needed to ensure that their supply, distribution and price accu-_
_rately represents the community members who are more invested in_
_[the project. This was observed in the recent Beanstalk exploit, where an](https://bean.money/blog/beanstalk-governance-exploit)_
_attacker used a flash loan to obtain a majority of governance tokens,_



_passing his own malicious proposal and quickly implementing it. The_
_voting mechanism worked well: but clearly, the voting weights did not_
_accurately reflect the community. To avoid such attacks, other plat-_
_forms such as Compound employ more fail-safes, such as a mandatory_
_waiting period before enacting the election result._


Instead of assuming that community-members would have an
implied incentive to positively contribute to their respective blockchain’s governance, sometimes a more direct approach is taken.
Participants are granted a decision-making right based on whether
they have positively contributed to the platform. What defines a
‘positive’ contribution is not always clear cut and its definition is
left to the platform’s community.


Definition 6 (Type 4: Meritocratic Suffrage). _A blockchain_
_governance system satisfies this property if it only guarantees decision-_
_making rights to participants who have positively contributed to the_
_platform._


Definition 7 (Type 5: Universal Suffrage). _A blockchain gov-_
_ernance system satisfies this property if it guarantees decision-making_
_rights to participants who have mining power or tokens in the platform_
_as well as participants with positive contributions to the platform._


We reiterate that it is not our objective to outline specific mechanisms for translating community-membership to voting power. For
example, we are not suggesting that an actor’s voting weight should
be more influenced by previous contributions than by an actor’s
stake in the platform. Instead, we are suggesting that it is important
that all forms of investments and contributions of a communitymember (which can be very different across different blockchains)
should be considered when formulating voting weight.
In this context, a mechanism that has gained traction recently in
the blockchain context is quadratic voting. In this mechanism, 1 vote
would cost 1, but 2 votes would cost 4 and so on. Such a mechanism
could achieve a better balance between what _Token-Based Suffrage_
and _Identity-Based Suffrage_ : having additional currency within the
system does entail enhanced voting rights, but some balancing
effect vis-à-vis the one-person one-vote rule seems appropriate. It
also provides a more flexible way of expressing voter preferences.
To see this, suppose that, in a governance system where votes can be
exchanged for tokens, two voters believe that one vote in favour of
some proposal is worth 5 and 10 respectively. By this, we mean that
the voters believe investing 1 coin for a vote, would yield a return

- n investment of 4 and 9 respectively. In the final election, if the
first voter is richer they could purchase 100 votes, while the second

- nly buys 3. This would signal that the first voter is particularly
in favour of this proposal, but in fact they bought more votes just
because they had a higher budget to spare. With quadratic voting,
the first voter would acquire 2 votes: the next vote would cost 4,
which is not seen as a profitable investment.


**2.2** **Pareto Efficiency**


Any blockchain governance system will necessarily depend on
a number of decision-making procedures: individual, competing
preferences have to be collected and combined into specific actions.
In this section we try to formalize how well the tools provided by
blockchain allow the _decision-makers_ (recall Definition 2) to reach
their most favourable outcome. Ideally, the result would the same as



64


SoK: Blockchain Governance AFT ’22, September 19–21, 2022, Cambridge, MA, USA




- ne chosen by an omniscient algorithm that has collected all their
private thoughts and magically chose the ‘perfect’ outcome. As we
will see, even the notion of a ‘perfect’ outcome is hard to define (and
under most definitions, does not always exist). We stress that this
might be _terrible_ for the community-members of the blockchain;
in this section we only focus on how well the intentions of the
decision-makers can be turned into actions. Aligning the intentions

- f the community-members and decision-makers is a question of
suffrage (as well as _Accountability_, which we define in Section 2.5).
The investigation of such decision-making processes is the focus of Social Choice Theory [35], which is an entire field of study
dedicated to them. One of its crowning early achievements is the
famous Arrow’s Impossibility Theorem (Arrow [26]), on voting
systems where participants _rank_ the possible candidates. Specifically, given a set of alternatives _𝐴_ = { _𝑎_ 1 _,𝑎_ 2 _, . . .,𝑎𝑛_ }, each voter _𝑖_
submits an ordered vector of the form _𝑎𝑖_ 1 ≻ _𝑎𝑖_ 2 ≻ _. . ._ ≻ _𝑎𝑖𝑛_ . Combining the votes should lead to an outcome preference ordering
_𝑎_ _𝑗_ 1 ≻ _𝑎_ _𝑗_ 2 ≻ _. . ._ ≻ _𝑎_ _𝑗𝑛_ - f the candidates that best represents the
voters. Unfortunately Arrow’s Theorem states that the following
natural properties cannot be satisfied at the same time:


  - If every voter prefers candidate X over Y, then X is ranked
higher than Y in the final outcome. This property is often
called _unanimity_ .

  - The order of X and Y in the final outcome depends only on
the ordering of X and Y in each voters preference, irrespective of how all other candidates are ordered. This is called

_independence of irrelevant alternatives_ .

   - There is no voter who has dictatorial control over the final

   - utcome.


Variations of this result have been adapted in many voting settings, even in cases where the voting process does not have to
reveal an entire ordering of outcomes (but only to select the ‘best’

- ne) or when voters have _cardinal_ preferences (i.e. they can assign
numerical preference values to each candidate). Note that almost
all popular voting schemes (such as _approval voting_, where each
voter selects a set of acceptable candidates) fall under these definitions. Perhaps the most famous of those impossibility results is the
Gibbard-Satterthwaite Theorem (Gibbard [46], Satterthwaite [64]),
roughly stating that any voting scenario with more than two candidates is either dictatorial, or subject to _strategic voting_ (i.e., voters
swaying the outcome by misreporting their actual preferences.
To deal with these impossibilities, the voting procedures used in
practice are not required to be optimal in every scenario, but to satisfy certain weaker properties depending on the setting. One such
mild property is _Pareto efficiency_ (e.g., [54, 62]). These properties
are tested assuming every voter truthfully reports their preferences.


Definition 8. _A blockchain governance system is Pareto efficient_
_if whenever a decision-making process is held, alternative X cannot_
_win if there exists another alternative Y that is preferred by at least_

_one participant and no participant prefers X over Y._


A Pareto efficient governance system would never lead to an

- utcome that is _clearly_ worse than another possible outcome. This
property should typically be satisfied (at least when interpreted
loosely, as some blockchain systems do not have an entirely rigorous
governance model), unless there is good reason not to. Evaluating



whether this property is satisfied can be tricky because a blockchain
governance system contains many interacting components, with
the final result seldom depending on a single vote. We make our
best effort to fairly evaluate how _likely_ it is that a Pareto efficient

- utcome is not selected and _how_ much worse is the selected alter
native.

_Approval voting_ is of particular importance, as it is the most
common voting mechanism used by the blockchains we evaluate.
Given _𝑛_ candidates, each voter can ‘approve’ as many as they want.
The winner is the candidate which was approved by most voters,

- ften combined with a threshold, such as also requiring approval
from at least 20% of them. Notice that even though the voters might
have ordinal or cardinal preferences, they can only submit a binary
signal for each candidate. Starting with a simple example, suppose
that 2 possible _incompatible_ blockchain updates _𝑎_ and _𝑏_ are up
for election. Furthermore, suppose that _every_ voter prefers _𝑎_ ≻ _𝑏_ .
The outcome will be dictated by the threshold they chose when
_converting_ their ordinal preferences to an approval vote. Typically
we would expect _𝑎_ to win, but _𝑏_ could win as well! Clearly, any
truthful voter who approved _𝑏_ would also approve _𝑎_, since _𝑎_ ≻ _𝑏_
for every voter. However, some voters might chose _not_ to approve
either of them. In this case _𝑏_ could win because of a tie. In fact, this
is the only way an outcome of approval voting might not be Pareto
efficient: if the winner is tied with the Pareto optimal candidate. This
happened because the voters where completely uniformed about
the preferences of each other and set their ‘approval threshold’
too high. The more information they have the less likely such an

- utcome becomes. A group of perfectly rational and informed voters
would always produce a Pareto efficient outcome. In addition, it is
important to keep in mind that there are two more ‘secret’ (implicit)

- ptions always available: to do _nothing_ - r to _fork_, which is to be
avoided. When combined with a minimum approval threshold and
some awareness on the part of the voters, the winner is most likely
either Pareto efficient, a suboptimal yet highly popular alternative

- r a deadlock. Finally, strategic voting involves setting the threshold
very high, which decreases the total number of votes and could
lead to a deadlock, but is unlikely to result in a fork.
We briefly discuss an alternative voting system that uses the complete _ordinal_ preference profile called _instant-runoff_ (IRV) voting.
It proceeds in turns:


  - From every ballot, only the top preference is counted.

  - If one candidate obtains a majority, they win.

  - Otherwise, the least popular top preference is deleted from
all ballots and the process repeats.


IRV is also not Pareto efficient as a good candidate might be deleted
early, if they fail to win many first choice votes. It is however
remarkably resistant to strategic voting [29] while retaining some
properties that approval voting lacks, such as selecting the majority
winner if one exists. This makes IRV particularly appealing when
the community is asked to choose between alternatives in a nonbinding way. The result can be further ratified by a referendum.
In some cases, IRV (and any voting system using ordinal preferences) might force the voters to inadvertently submit misleading
information. For example, IRV assumes that the first and second
place candidate on every ballot are separated by an equal amount,
whereas some voters might be indifferent while others strongly in



65


AFT ’22, September 19–21, 2022, Cambridge, MA, USA


favour of their first choice only. Approval voting sometimes gets
around this issue by asking for even less information. Ordinal preferences can be easily elicited by an _auction_ which is undesirable for
an election. A better alternative is to use an ordinal voting mechanism such as majority judgment [28] or combine approval voting
with _token locking_ : voters who feel strongly about some candidate
may lock their vote tokens for longer, indicating that this election
is particularly important to them.


**2.3** **Confidentiality**


One of the initial goals of Bitcoin, as well as arguably the first design
consideration when implementing a voting system on which the
governance system will be based, is the approach to _privacy_ . While
its definition is fairly intuitive, we make a distinction between
_secrecy_ and _pseudonymity_ .


Definition 9 (Type 1: Secrecy). _A blockchain governance system_
_satisfies secrecy if whenever a decision-making process is held, an_
_adversary cannot guess the input of any participant better than an_
_adversarial algorithm whose only inputs are the overall tally and, if_
_the adversary is a participant, the adversary’s input._


This definition follows from the early work of Benaloh, cf. [39]
and has been formally modeled in numerous subsequent works,
e.g., see the model of Juels et al. [50]. This is the strongest of the two
notions and typically what would be required of an offline voting
system (e.g., traditional elections in most countries). Often, true
secrecy is difficult to accomplish in a decentralised setting or might
be undesirable. For example, many blockchain combine on-chain
governance with _off-chain_ elements, such as discussions on forums.
These discussions may be part of the formal governance model and
could be combined with an off-chain poll, based on the on-chain
distribution of voting power. In these cases there could be a benefit
in using _pseudonyms_, keeping the real life identity safe but tying
their public discourse with their actual vote. This is particularly
relevant when the distribution of voting power distribution. Even
though not explicitly mentioned by name, the Bitcoin white paper
provides an explanation about why _pseudonymity_ [57] might be a
good enough alternative.


Definition 10 (Type 2: Pseudonymity). _A blockchain gover-_
_nance system satisfies pseudonymity if no participant is required to_
_reveal their real-life identity to participate in the decision-making_

_processes._


The reason for the development of this notion is that blockchain
systems are usually designed with the assumption that consensus
is achieved _only_ with regards to the shared ledger; it is impossible
to keep track of any information outside of it. Therefore, the same
techniques used to keep track of the distribution of wealth (e.g.,
publicly announcing and linking transactions together), can be
used to provide voting rights to the people actually involved in the
blockchain without requiring much additional work. This is further
related to the notion of _suffrage_, which is defined in Section 2.1. For
example, in Proof-of-Stake based cryptocurrencies like Cardano,
voting rights for some applications are distributed based on the
amount of _stake_ held by each user, as outlined in the paper by Zhang
et al. [70] describing the voting system used by the treasury system

- f that platform. In practical terms, as long as the cryptographic



information required when first producing one’s online identity
cannot be traced back to any real-life information, pseudonymity
is satisfied. Privacy can be further strengthened, considering the
notion of _coercion-resistance_ [41, 50].


Definition 11. _A blockchain governance system satisfies coercion-_
_resistance if whenever a decision-making process is held, a participant_
_can deceive the adversary into thinking that they have behaved as_
_instructed, when the participant has in fact made an input according_
_to their own intentions._


In a strict sense, this definition is arguably stronger than the
guarantee provided by traditional elections: the voter should be able
to deceive the adversary even about his participation, not just his
vote. By definition, this exceeds the notion of privacy and requires
at least one _anonymous_ channel of communication. Such a scheme is
described in [50], but tallying requires an amount of communication
which is quadratic in the number of votes. As such, this property
is typically too demanding to be fulfilled in a blockchain setting,
for most applications. However, it can be partially satisfied (e.g.,
if a ballot is encrypted in a way such that the voter can verify its
inclusion when it is cast, but it is impossible for him to reclaim it
later, if asked to prove that they voted in some way — the fact that
this only provides partial fulfillment of the property stems from the
fact that if the participant’s device leaks the random coins, then the
ciphertext can be demonstrated to encode the participant’s input).


**2.4** **Verifiability**


To complement confidentiality, we now need a property that goes
in the opposite direction, namely _verifiability_ . This is a crucial
property of every voting system, as it legitimises the election result.
The widely accepted “golden standard” of verifiability is expressed
below in the form of end-to-end verifiability.


Definition 12 (End-to-End Verifiability). _A blockchain gov-_
_ernance system is verifiable if whenever a decision-making process_
_takes place, participants are to able to verify their inputs were properly_
_tallied and independent observers are able to verify that inputs from_
_eligible participants were properly tallied._


Furthermore, Gharadaghy and Volkamer [45] split the definition

- f verifiability into two separate notions.


  - **Individual Verifiability:** It is possible for the voter to audit that his/her vote has been properly created (in general
encrypted), stored, and tallied.

  - **Universal Verifiability:** Everyone can audit the fact that

    - nly votes from eligible voters are stored in a ballot box, and
that all stored votes are properly tallied.


At a high level, a system satisfying both properties would be called
end-to-end verifiable – but we refer to [40] for more details on the
notion of verifiability as well as the subtleties that arise in defining
the concept formally.
Intuitively, satisfying privacy (and Definition 9 in particular) as
well as coercion-resistance definition 11 should make verifiability
more difficult to achieve. After all, these two limit the amount of information that a third-party could elicit by observing the blockchain.
Despite this, it is indeed possible to achieve both to a certain adequate level. As exemplary schemes we can point to the work of



66


SoK: Blockchain Governance AFT ’22, September 19–21, 2022, Cambridge, MA, USA




[50] mentioned earlier, but also schemes such as the early work of
Benaloh and Tuinstra [33], the Benaloh-challenge approach [32]
that has influenced a lot of practical e-voting systems, see e.g., [53],

- r the hardware token based approach of [24]. This latter work also
provides a comprehensive modeling of the concept of incoercibility
that extends well beyond the setting of e-voting per se and can be
immediately applicable to the blockchain setting as well.


**2.5** **Accountability**


The quest for accountability in governance is not a recent pursuit,
as it was clearly recognised by the ancient Egyptians and the ancient Greeks [43]. Since then, accountability as a concept has been
split into multiple types and dimensions. For example, Grant and
Keohane [47] outlines that accountability can take two general
forms: vertical (where a party is accountable to other parties that
are higher in a given hierarchy) and horizontal (where a party is
accountable to other parties that are not higher or lower in a given
hierarchy). Although _collective_ accountability is often implicitly
implied in coin-based voting, _individual_ accountability is not. That
is, if enough voters vote for a bad decision, the coin value of every
voter declines whether or not they supported the decision. Individual accountability can take various forms, the most prominent of
which is often referred to as ‘skin in the game’, where participants
have an individual investment that will be directly affected by their
individual actions.

Even though only the decision-makers take part in governance,
accountability should capture the possible harm incurred to the
community-members as well. This is an added layer of security
required to align the incentives of these two types of participants,
particularly in governance designs where the two groups could be
disjoint (e.g., voting rights based on a governance token that has
no other function or direct relation to any on-chain activity).


Definition 13. _A blockchain governance system satisfies the prop-_
_erty of accountability if whenever participants bring in a change, they_
_are held individually responsible for it in a clearly defined way by the_
_platform._


Examples outside the blockchain space include the work done in
Sacco et al. [63], where participants review publications and those
having more ‘skin in the game’ (evaluating publications in which
they will be marked as co-authors) have an increased individual
interest in ensuring that a study’s ambiguously reported methods
and analyses are clarified prior to submission. Examples in the
blockchain space include Polkadot’s governance system [8], where
voters who vote in favour of a proposal will have their stake locked
until the proposal is ‘enacted’ or deployed.


**2.6** **Sustainability**


Changes in blockchain governance rely on two main actors: those
who develop and propose the changes, and those who decide on
whether or not to adopt these changes. Contributions from both actors help the platform to adapt and evolve and need to be rewarded.


Definition 14 (Sustainable Development). _A blockchain gov-_
_ernance system sustains development if it incentivises, via monetary_
_rewards or otherwise, participants who develop successful improve-_
_ment proposals for the platform._



Definition 15 (Sustainable Participation). _A blockchain gov-_
_ernance system sustains participation if it incentivises, via monetary_
_rewards or otherwise, participants who participate in the decision-_
_making process of the platform._


Remark. _Sustainability is different from accountability in both_
_moral and practical terms. Contrary to the definition of Accountability,_
_Sustainability rewards development or participation with no regard to_
_its outcome (ideally, before the respective agents have to perform the_
_work or incur any costs). Accountability relates to possible penalties_
_applied afterwards, once the effects of a particular change are apparent._
_For example, rewarding users just for voting would somewhat enable_
_sustainable participation, but would not qualify for accountability._
_On the contrary, penalizing voters who approved a malicious proposal,_
_without ever rewarding anyone, would only meet the definition of_
_accountability._


The idea behind having participation and development incentives in place is to _help_ justify the cost of engagement, which can
lead to higher voter participation or more contributions to the
platform. These incentives can take various forms, from monetary
incentives to reputation- or merit-based incentives [71]. However,
Sustainable Participation could be a double edged sword if applied
carelessly (e.g., [58, 65]. A monetary reward that is too small might
convert a moral decision into a financial one, paradoxically decreasing participation. While in general increased participation
also leads to an increase in information acquisition from the voters,
it is certainly more beneficial to have a smaller set of participants
that have done their due diligence and vote as honestly as possible,
than a larger group of disinterested individuals who cast votes at
random just to collect rewards.


**2.7** **Liveness**


In formal, on-chain governed platforms, the process for proposing
and adopting changes is often constrained by fixed-length time
periods. An example of this is Tezos’s Granada protocol [9], where
a proposal has to go through five governance cycles (each lasting
roughly two weeks) in order to be adopted. In such platforms, an
unforeseen event that requires urgent action will not be resolved
promptly through the platform’s governance process. Therefore,
a blockchain governance system must not only be able to process
regular changes, but also urgent ones.


Definition 16. _A blockchain governance system satisfies live-_
_ness if it is capable of incorporating an input of urgency from the_
_stakeholders and then being capable of acting on it in the sense that_
_if an issue is deemed to be urgent according to some function, then_
_the decision making procedure is capable of terminating within a_
_reasonable amount of time, as a function of the urgency of the matter._


This definition includes having some protection against _denial of_
_service_ attacks, that would prohibit governance mechanisms from
terminating in time. All systems evaluated in this work are safe, at
least from a high level standpoint, ignoring implementation details.
Events like the DAO hack [1] have shown the need for blockchain
governance systems to be able to accommodate inputs of urgency
and act on them within a suitable amount of time. An example of
blockchain governance system with liveness measures is Polkadot

[8], which allows for emergency referendums to be initiated by



67


AFT ’22, September 19–21, 2022, Cambridge, MA, USA


an assigned technical committee. Others, such as MakerDAO, implement an emergency shutdown functionality: since it is running

- n Ethereum, in an emergency the smart contact can suspend its
normal operation and return the invested assets to their owners.


**3** **EVALUATIONS**


In this section, we evaluate a number of popular platforms with
respect to the properties outlined in Section 2. The platforms below
were chosen such that they present an overview of current approaches. An overall view of the evaluations can be found in Table
1. We start with Bitcoin and Ethereum, two of the oldest and most
influential blockchains. These two use proof-of-work for consensus
and rely mostly on their developers for governance, who maintain
a connection with the community but ultimately have control over
the direction of the platform. Continuing, we consider Tezos, Polkadot and Decred. The first two use proof-of-stake, while Decred takes
a hybrid approach. In particular, whereas Tezos and Decred favour
“direct” democracy, Polkadot uses a _council_ as well, representing
two fundamentally different approaches to managing how voters
express their preferences and interact with the governance process.
Next, we study Project Catalyst and Dash, which incorporate a treasury in their decision making, meaning that the result of the voting
process needs to respect a budget. Finally we consider Compound,
Uniswap and MakerDAO that use a governance token approach. In
the case of Compound and Uniswap this token is purely used for
voting, while for MakerDAO it also supports the normal operation

- f the Maker protocol.
Gathering all the necessary information about every governance
system is not always easy: typically, the platform’s white paper
would contain a very high level overview. Moore details can sometimes be found on the websites of the respective blockchains, but

- ften the complete picture can only be acquired by interacting with
a wallet, voting app or forum. Keeping that in mind, we have made

- ur best efforts to cite the relevant sources.


Remark. _Due to size constraints, in the main text we include only_
_a high level evaluation of some of the governance protocols. A more_
_in-depth, up-to-date study, along with a point-to-point comparison_
_with respect to each property can be found in the full version of this_
_paper [52]._


**3.1** **Bitcoin**


Bitcoin [57] is the most prominent blockchain platform and it is
a proof-of-work, mostly off-chain governed blockchain. The Bitcoin Improvement Proposal (BIP) process [10] is Bitcoin’s primary
mechanism for ‘proposing new features, for collecting community
input on an issue, and for documenting design decisions’. An individual or a group who wishes to submit a BIP is responsible for
collecting community feedback on both the initial idea and the BIP
before submitting it to the Bitcoin mailing list for review. Following
discussions, the proposal is submitted to the BIP repository as a pull
request, where a BIP editor will appropriately label it. BIP editors
fulfill administrative and editorial responsibilities. There are repository ‘maintainers’ who are responsible for merging pull requests,
as well as a ‘lead maintainer’ who is responsible for the release
cycle as well as overall merging, moderation and appointment of
maintainers [11]. Maintainers and editors are often contributors



who earnt the community’s trust over time. A peer review process
takes place, which is expressed by comments in the pull request.
Whether a pull request is merged into Bitcoin Core rests with the
project merge maintainers and ultimately the project lead. Maintainers will take into consideration if a patch is in line with the
general principles of the project; meets the minimum standards
for inclusion; and will judge the general consensus of contributors

[11].
There are stages through which a BIP can progress, including
‘Rejected’ and ‘Final’. In progressing to a status of ‘Final’, there are
two paths:


  - _Soft-fork BIP_ . A soft-fork upgrade often requires a 95% miner
super-majority. This is done via an on-chain signaling mechanism introduced in [12].

  - _Hard-fork BIP_ . A hard-fork upgrade requires adoption from
the entire ‘Bitcoin economy’, which has to be expressed by
the usage of the upgraded software.


**Evaluation.** It is important to note here that the Bitcoin decisionmaking mechanism is informal, at least with respect to other platforms. Clearly, the on-chain aspects of Bitcoin’s governance satisfy
pseudonymity, but not secrecy or coercion resistance as no ‘votes’
are even encrypted. The same is true for its off-chain component.
This has the advantage that the system is mostly verifiable, even
though having part of the deliberation take place in public forums
is harder to track and could be an impermanent storage solution.
Since the decision-making process is informal, without clearly defined structure or voting rules, Pareto Efficiency (to any degree)
cannot be guaranteed. Sustainability and Accountability fail for the
same reason, as there are no defined rules for either. Liveness is
arguably partially satisfied, given the informality and flexibility of
the BIP system. Since miners are guaranteed to explicitly signal
their approval or disapproval of soft-fork upgrades [12], miningbased suffrage is satisfied. Although those with previous positive
contributions and relevant expertise are able to provide substantial
inputs in the decision-making process, there is no explicit guarantee

- f their decision-making rights due to the informality of the process. Despite this, we conclude that meritocratic suffrage is _likely_
satisfied.


**3.2** **Ethereum**


Ethereum [13] is one of the most significant second-generation
blockchain platforms. Starting as proof-of-work and transitioning

- n 15 September 2022 to proof-of-stake (PoS) it is governed offchain, using the Ethereum Improvement Proposal (EIP) process

[14] as a mechanism for proposing and integration changes. It is
almost identical to that of Bitcoin, without giving miners the option
to signal their preferences on-chain.


**3.3** **Tezos**


Tezos [15] is a proof-of-stake, on-chain governed blockchain platform, which defines its governance process as ‘self-amending”. Contrary to Bitcoin or Ethereum, participating in governance is based

- n _stake_ . Specifically, Bakers (also known as _delegates_ ) need to have
at least 8 _,_ 000 XTZ (called a _roll_ ) and the infrastructure to run a
Tezos node in order to gain _both_ block producing and voting priviledges. Community members who have fewer than 8 _,_ 000 XTZ or



68


SoK: Blockchain Governance AFT ’22, September 19–21, 2022, Cambridge, MA, USA



**Platform** _Suffrage_ _Pareto Efficiency_ _Confidentiality_ _Verifiability_ _Accountability_ _Sustainability Liveness_


**Bitcoin**

**Ethereum**

**Catalyst**
**Dash**

**Tezos**

**Polkadot**

**Decred**

**Compound**
**Uniswap**
**Maker DAO**

**Table 1: Overview of the evaluations of each property against each of the chosen platforms.** Every platform might satisfy each
property to a different degree, shown by appropriately filling each circle.



are unwilling to spend the computational resources can _delegate_
their stake to bakers, who produce blocks and vote on their behalf.
The voting process is currently divided in five governance periods,
each period spanning roughly two weeks: Proposal, Testing-vote,
Testing, Promotion-vote and Adoption. During the proposal period,
_approval voting_ is used to select the winning proposal, which must
also be accepted by at least 5% of the total vote. In testing-vote and
promotion-vote the possible options are ‘Yea’, ‘Nay’ or ‘Pass’. A
quorum between 0 _._ 2 and 0 _._ 7 of the total stake need to be reached,
and the proposal is implemented if an 80% supermajority of ‘Yea’ is
reached.

**Evaluation.** As with Bitcoin, Tezos only satisfies Pseudonymity,
but is completely verifiable. Pareto Efficiency is more nuanced. If a
proposal receives less than 5% of the upvotes or is tied with another
proposal, no proposal will pass, even though operators could have
voted for some proposals. However, given the properties of approval
voting outlined in Section 2.2, this effect is mild. In addition, the
selected outcome is checked once again at the last step. Pareto
efficiency could be further hampered under the assumption that
the proposals appearing in a single voting period are _too many_

- r _too technical_ to evaluate in the allotted time, before the vote.
This could make voters inadvertently split their votes and abstain

- n many proposals, either leading to a deadlock if no proposal
reaches 5% or favoring _whales_ (i.e. users with many tokens). To
see this, consider that between 3 proposals _𝐴, 𝐵_ and _𝐶_ - ne whale
with 40% of the tokens favours _𝐴_ while every other user equally
likes _𝐵_ and _𝐶_, but dislikes _𝐴_ . If the whale votes in favour of _𝐴_
and the other voters evenly split their votes between _𝐵_ and _𝐶_, _𝐴_
could win the election. A possible solution to this would be to
separate _vote_ from _stake_ delegation. Voters could transfer their
voting rights to more knowledgeable individuals that they trust
which could consolidate their votes, while retaining their block
production capabilities. Accountability or Sustainability are not
satisfied. Given the lack of flexibility of the on-chain governance
model, the Tezos governance system is incapable of taking inputs of



urgency. Although a Gitlab issue or a pull request could be initiated
without going through the formal on-chain route, it is still not the

- fficially documented, and certainly not the ‘self-amending”, way
by which the system processes inputs.


**3.4** **Polkadot**


Polkadot [8] is a proof-of-stake, _mostly-on-chain_ governed blockchain platform with a number interesting additions, including an
elected council and a technical council. Voters require at least 5
DOT to participate in governance and their voting power is based

- n stake. At a glance, the voters elect councilors, directly vote on
referendums and submit proposals. The councilors then have the
power to _veto_ dangerous proposals, elect the technical committee,
submit proposal of their own for approval by the voters and also
control the _treasury_ . The technical council can submit _emergency_
referendums, that are implemented immediately if approved.
More specifically, the council consists of 13 members with 7 day
tenures. They are elected using an approval voting based method,
the weighted Phragmén election algorithm (e.g. [36]. An in-house
refinement of Phragmén called Phragmms [38] could be used in
the future. During a referendum election, an _adaptive_ quorum is
used, requiring a different majority and turnout based on how the
referendum was created (e.g, by the community or a weak council
majority). A successful referendum enters a 28 day waiting period
before enactment, unless it is an emergency. Typically, the votes cast
are _locked_ for these 28 days. However, the voters can increase their
voting power by voluntarily locking them for longer (or decrease
it by not locking at all). The treasury is controlled by the council,
which decides whether to allocate funds to proposals that ask for
them based on current supply.
**Evaluation.** Only pseudonymity and verifiability are satisfied.
The council elections and referendums are Pareto efficient. In ad
dition, the voters can signal the strength of their preferences by
locking their votes for an extended time. Voting in favour of a proposal requires funds to be locked in until the proposal is enacted.



69


AFT ’22, September 19–21, 2022, Cambridge, MA, USA


The documented rationale behind this is to hold voters responsible for a proposal that they vote for, satisfying accountability
and further reinforcing Pareto Efficiency. There are no explicit or
direct rewards given for participation or contribution to satisfy
sustainability. However, Polkadot have deliberately chosen _against_
[monetary rewards for voters, for justified reasons (as detailed in](https://polkadot.network/blog/a-walkthrough-of-polkadots-governance/)
Section 2.6). However, council members should probably receive
some direct compensation. Even though their tenure is short, they
hold a lot of power and should have the ability to devote themselves
full time. The Polkadot governance mechanism is capable of taking
in inputs of urgency (i.e. emergency referendums) and acting on it
if deemed urgent by the council, all whilst being able to terminate
within an amount of time proportional to the urgency. Token-based
suffrage _is_ satisfied since only token holders are allowed to vote.
The council adds teams to the technical committee (which is able to
propose emergency referendums) based on their positive technical
contributions and expertise. However, those teams are chosen by
council members only and a positive contribution does not equate
to a guarantee of an input in a decision-making process.


**3.5** **Decred**


Decred is a hybrid proof-of-work and proof-of-stake system that
is mostly on-chain governed [16]. Voters can participate in governance by locking enough DCR, which is the native token of Decred.
This provides them with _tickets_ which supplement the consensus
protocol and can also be used for voting. High level issues that
require funds from the Decred Treasury are handled off-chain, in
[Politeia. This deliberation results in an election which is crypto-](https://proposals.decred.org/)
graphically coupled to a snapshot of the chain. A 20% quorum is
needed, with over 60% of the votes being in favour. The on-chain
component is the Decred Change Proposal (DCP) [17], through
which the consensus mechanism is updated. This requires a 10%
quorum and 75% majority of approval. Failing to meet the quorum,
the election will be repeated in the next cycle. If it is successful, a
‘lock-in’ period begins, after which all nodes should update their
software.

**Evaluation** The votes are not encrypted, therefore only pseudonymity and verifiability are satisfied. Pareto efficiency is somewhat
satisfied: there are similar issues as Tezos, but the added role of
Politeia could improve the outcome. Sustainable development is
satisfied (somewhat informally) but there are no specific rewards
for participating in governance. Voters receive rewards, but these
have to do with their role in the hybrid consensus protocol. Accountability could be improved, as the token locking required for
voting is shorter than the timelock for successful proposals.


**3.6** **Compound**


Compound [18] is a protocol running _on_ the Ethereum blockchain
that establishes money markets. Governance in Compound is fueled
[by an ERC-20 compatible token called COMP [19]. These](https://etherscan.io/token/0xc00e94cb662c3520282e6f5717214004a7f26888) _gover-_
_nance_ tokens are distributed to the community through various
channels: some are allocated to users based on their invested assets,

- thers to Compound Labs Inc. shareholders and employees, etc.
Holding COMP allows users to vote, delegate to others and create
proposals, which are executable pieces of code. Once submitted,
these proposals enter a two day review period, following a three



day election. A proposal is successful if a majority is in favour and
a quorum is reached. After that, the proposal is _locked_ for two days
before implementation, for security. Finally, the _Pause Guardian_
(controlled by a community appointed multi-signature) can suspend
most functionalities of Compound at any time.
**Evaluation** Every step of the governance process is performed by
interacting with smart contracts on Ethereum, without any further
cryptographic techniques, satisfying pseudonymity and verifiability.
Once a proposal enters the voting phase, the voters only have two

- ptions: yes or no, which is clearly Pareto Efficient. If there are
multiple incompatible options (e.g., values of a specific parameter),
these proposals would have to be dealt with sequentially: the actual

- rder could bias voters, which complicates their decisions and leaks
information. Therefore, Pareto Efficiency is somewhat satisfied (e.g.,
between two highly popular proposal, the slightly less popular one
might win if it is up for election first and then the users might
be less eager to implement another change). Once a proposal is
executed, its creator and voters are completely independent from
its future and there are no rewards associated with the process.
Therefore, neither availability or sustainability are satisfied. The
total time between creating a government proposal and voting
for it takes 7 days, 2 of which are hard-coded into the Timelock.
This window for immediate action is only open right after a vote,
but adding the Pause Guardian, liveness is satisfied. Since voting
eligibility depends only on having COMP tokens, which can be
exchanged and are initially distributed to addresses with assets on
Compound, token-based suffrage is satisfied. Some COMP tokens
are distributed or reserved for members of the Compound team.
Therefore, meritocratic suffrage is slightly satisfied.


**3.7** **Maker DAO**


Maker DAO [20] is a decentralized organization running on Ethereum and based on the Maker Protocol. One of its features is using
a two-token system, with DAI, which is a stablecoin pegged to the
U.S. dollar, and MKR as the governance token. MKR also serves an
additional purpose: to support DAI’s peg. The governance system
employs both on and off-chain elements. The off-chain component
[takes place at the Maker DAO forum, where users can create Forum](https://forum.makerdao.com/)
Signal Threads, which are followed by a poll. Each forum user has a
single vote, irrespective of MKR. These are further ratified on-chain
by Governance Polls, which employ _instant-runoff voting_, weighted
by the MKR of each voter. Finally, changes to the protocol (which
are pieces of executable code) are enacted by Executive Votes. These
follow a _continuous_ approval vote system, with the most approved
Vote at any given time being the actual implementation. For security
reasons, these changes happen after a 24 hour waiting period and
there is also an emergency shutdown functionality, triggered if the
community locks enough MKR.
**Evaluation.** As there is no vote encryption, only pseudonymity and
verifiability are satisfied. Pareto Efficiency is improved compared to

- ther designs by using instant-runoff voting to handle competing
proposals, thus giving voter a richer action space to declare their
preferences accurately. Suffrage is also improved, as there is a clear
connection between MKR tokens and the overall functionality of
Maker DAO, further coupling its value to some actual generated
utility.



70


SoK: Blockchain Governance AFT ’22, September 19–21, 2022, Cambridge, MA, USA



Remark. _Project Catalyst and Dash include a_ treasury _. Funds are_
_collected during the normal blockchain operation and allocated to_
_fund its development and other projects. The voter preferences are_
_more complicated, since each proposal needs to be weighed against its_
_budget and the opportunity cost of funding it. Decred also includes a_
_treasury, but proposals are first debated off-chain, rather than set to_
_compete on-chain for some portion the budget available in one round_

_of funding. The final vote_ is _on-chain, but only to confirm proposals_
_that already have off-chain support._


**3.8** **Project Catalyst**


Project Catalyst [21] is the on-chain treasury governance system
used by the Cardano blockchain, which is proof-of-stake. Governance takes place in twelve week periods called funds and involves
a number of additional agents, on top of the usual voters, whose
voting power and eligibility is dependent on stake ownership. At
the beginning of the fund, community generated proposals (which
include a corresponding budget) are submitted. These are then
reviewed by Community Advisors (CA’s) and these reviews are
further checked for their quality by veteran Community Advisors
(vCA’s), both of which are rewarded for their efforts. Given these
evaluations, an approval voting based mechanism [70] is used. The
proposal whose ‘Yes’ votes minus the ‘No’ votes are more than 5%

- f the total votes received is eligible for funding. These eligible proposals are then sorted according to their approval. If the available
funds are not enough to cover some proposal, it is skipped and
a less popular (but cheaper one) could take its place. In addition,
there is the Catalyst Circle [22], an elected group of representatives
that oversees Catalyst and a delegated voting system is proposed
for future iterations.

**Evaluation.** Everyone participates in Project Catalyst using
their wallet address. Voters submit _encrypted_ ballots (padded with
some randomness), using the public key issued by a committee,
which tallies the votes and decrypts the result. If the voter address
is linked to a real identity, the only information available is that
this particular person voted, keeping the contents secret. The ballot
itself cannot be decrypted by the voter and if the random padding
is not kept, it is impossible even for the voter to convince anyone

- f the way they voted. The result of the vote can be independently
verified and long as the voter saved the random padding, they can
verify that their particular vote was counted. Therefore, there is a
(somewhat contrived) sequence of events after which a voter would
be unable to check that their ballot has been added.

In some cases, proposals with fewer votes will be prioritised
for their lower budgets. For example, if the total fund is 100 and
the three winning proposals have budget 1, 50 and 50 (in order of
popularity) the last proposal will not receive funding, even though
every voter might prefer funding the two 50 proposals. Additionally,
each voter could submit an uninformative ‘no’ vote to many proposals, in order to maximize the winning chance of their favourite.
A potential mitigation would be to use techniques from Participatory Budgeting [31] and Distortion [25], which use a small amount

- f _ordinal information_ (e.g., asking voters to compare between 2
proposals or to list their most favourite one) to improve the quality

- f the outcome. Overall, Pareto Efficiency is _somewhat_ satisfied.



There are no explicit, on or off-chain, penalties. Proposers need
to submit progress reports about their projects to keep receiving
funding and community advisors can be penalized for poor reviews

- r absence. As these are centralized or community-driven without
clearly described mechanisms, accountability is mostly _not_ satisfied.
Although there is no explicit reward given to the proposer, it is
her responsibility to request the amount which cover the cost of
her work. All other parties are rewarded for participating in the
governance process and to an extent receive larger rewards for
additional effort. Each Project Catalyst Fund follows a 12 week
timeline. Liveness is not satisfied: even though the funds can be
released in accordance with each proposal’s progress, there is no
mechanism to take urgent action. Voting rights depend only on
having at least 500 ADA. There are no guaranteed voting rights
based on previous positive contributions, however, community
advisors can affect the outcome of the votes through their reviews.


**4** **CHALLENGES & RESEARCH DIRECTIONS**


It should be clear from our exposition so far that the blockchain
governance space is still rife with challenges and open questions.
We summarize in this section a number of them to motivate future

research in the area.

_I. Tradeoffs between Privacy vs. Verifiability and Suffrage._ The
tension between verifiability and privacy stems from requirements
such as universal verifiability which mandates tracing each decision
back to the inputs of decision-makers as determined by suffrage.
The higher degree of privacy that is required, the more difficult it is
to ensure verifiability; as a simple example from classical elections,
if the electoral roll remains private, then it is difficult for an external

- bserver to verify whether the correct set of decision-makers has
participated. This also creates a tension with suffrage as types

- f suffrage that maximize inclusion, for the sake of verifiability,
might have to expose a larger set of community-members that

- therwise would have remained private. Technically reconciling
these properties is highly non-trivial, especially if privacy aspects
such as coercion resilience are desired.

_II. Proofs of Personhood, Identity-based suffrage and tradeoffs with_
_Privacy ._ While there is wide agreement that individual users should
have equal weight in decision-making (something advocated in the
context of election reform for centuries, cf. [48]), achieving this
type of suffrage is particularly challenging in the context of decentralized systems. Even though some initial work is undertaken in
this direction e.g., [66], and there are also connections with other
concepts in cyber-security such as CAPTCHAs [69], nevertheless
the problem of achieving a satisfactory level of identity-based suffrage in the context of blockchain governance is still wide open.
This challenge should be also considered from the lens of privacy,
since in many cases of such proofs, community-members would
have to reveal personally identifiable information to other actors
something that comes inevitably with privacy implications.
_III. Meritocratic suffrage and tradeoffs with privacy._ The challenge
in the context of meritocratic suffrage is in two levels, first, in
quantifying what type of merit itself should warrant participation to
decision-making. The second level is recording reliably the relevant
actions of community-members in the system so that it can be
acted upon during the decision-making process. Finally, as in the



71


AFT ’22, September 19–21, 2022, Cambridge, MA, USA


case of proofs of personhood, there can be privacy implications.
Some early works in this direction show that privacy and merit
may be reconciled, see e.g., the signatures of reputation primitive

[34] but still, significantly more work is required to fully tackle the
full spectrum of possible ways to express and act on merit.
_IV. Exchanges, venture capital investors and token-based suffrage._
In the setting of token-based suffrage, an important consideration is
the fact that token-holders may choose custody solutions for their
tokens (e.g., reducing risks regarding loss of keys, or the ability to
access services or rewards provided by custody operators). While
among some cryptocurrency users this is frowned upon (the tenet
“not your keys, not your coins” is frequently repeated in social
media) there is a large number of users that prefer to keep their
digital assets in third party providers’ systems. [2] This results in
entities with inflated leverage in a token-based system that in some
cases can control a very significant portion of the token supply. A
related issue is the presence of venture capital firms that are early
investors in some platforms and receive a large amount of tokens
at preferential prices in exchange for funding initial development
efforts. This similarly may result in increased leverage which can
be perceived as unfair by other community-members.
_V. Rational ignorance and inaction._ Rational ignorance [67] is
when decision-makers refrain from acquiring the knowledge required of meaningful input when voting, or when delegating their
vote, due to the fact that the cost of acquiring that knowledge exceeds any expected potential benefits. A similar argument can be
applied to developing improvement proposals, where inaction can
be more rational than action if the cost of development (or even the
act of preparing a proposal) exceeds any potential benefits. These
issues pertain to the property of sustainability which so far lacks a
comprehensive theoretical framework in the context of blockchain
governance. For some recent work in this direction see [60, 61].
_VI. Tradeoffs between accountability and utility._ Recall that making
decision-makers accountable suggests some degree of “skin-in-the
game” on their side and the natural way to achieve this implies
some form of restriction of the functionality that is offered to them.
As a result, the immediate utility that decision makers can extract
from the platform is reduced — recall the example of “token lockup”
for the duration of a certain decision making process. The main
challenge in this setting is to model and quantify the relevant aspect

- f this utility reduction and mapping the spectrum of possible

- ptions so that the right balance between accountability and utility
can be determined on a case by case basis.
_VII. Tradeoffs between Liveness vs. Pareto Efficiency and Suffrage._
As discussed in the context of liveness, expedient decision-making
is highly desirable. Unfortunately high expediency can come at

- dds with Pareto efficiency: if decision-makers have preferences
which are not recorded due to the system not giving them enough
time to react, Pareto efficiency could be affected (notice that abstaining can be also a preference, but there is a distinction between
having an actual preference and missing the deadline to provide
it). Liveness can also exhibit a similar tradeoff with suffrage: the
more exclusive the suffrage mapping from community-members to


2Indicatively, statistics from the web-site https://cryptoquant.com/, at the time of
writing (May 2022), suggest that about 13 _._ 3% of the Bitcoin supply is held on exchanges.
The figure for Ethereum is higher at slightly above 20%.



decision-makers is, the higher the expediency of the system may become - but this of course comes at the expense of the system being
less inclusive. Striking the right balance between these properties
is another question on which future research should focus.


**5** **CONCLUSION**


In this work we focused on systematizing the core properties of
blockchain governance. We took a first principles approach and
derived seven fundamental properties using which we analyzed a
number of widely used blockchain platforms. There are also other
platforms that we attempted to cover, but these were either too
poorly documented or were yet to implement governance mechanisms. We consider our work to be a comprehensive coverage of
popular blockchain systems at the time of writing.
The main outcome of the systematization effort, as illustrated in
Table 1, is that in many ways all current blockchain platforms either
have deficiencies in their governance processes or allow significant
room for improvement. It is worth reiterating that achieving all
stated properties to the highest possible degree is impossible due to
their conflicting nature and as a result it is inevitable that platforms
must decide on appropriate tradeoffs between the various properties
that are the most suitable for each particular setting. Arguably,
without effective governance processes, blockchain technology will
fail to reach its full potential. For one thing, software engineering
practice has shown that software updates, extensions and patches
are a necessity in the lifecycle of computer systems and as a result,
without proper governance, blockchain systems will fail to adapt to
unanticipated use cases and mitigate software bug vulnerabilities
that are inevitably discovered in any system.


**REFERENCES**


[1] Divisions of Corporation Finance and Enforcemen. Statement by the Divisions of
Corporation Finance and Enforcement on the Report of Investigation on the DAO.
[Investigation report. July 2017. URL: https://www.sec.gov/litigation/investreport/](https://www.sec.gov/ litigation/investreport/34-81207.pdf)
[34-81207.pdf.](https://www.sec.gov/ litigation/investreport/34-81207.pdf)

[2] Almost $500,000 in Ethereum Classic coin stolen by forking its blockchain, Dan
Goodin, 1/8/2019, Arstechnica.

[3] Legal operational and technical standards for e-voting, Recommendation
Rec(2004)11 adopted by the Committee of Ministers of the Council of
Europe on 30 September 2004 and explanatory memorandum, Council of
[Europe publishing, 2004, http://www.eods.eu/library/CoE_Recommentaion%](http://www.eods.eu/library/CoE_Recommentaion%20on%20Legal,%20Operational%20and%20Technical%20Standards%20for%20E-voting_2004_EN.pdf)
[20on%20Legal,%20Operational%20and%20Technical%20Standards%20for%20E-](http://www.eods.eu/library/CoE_Recommentaion%20on%20Legal,%20Operational%20and%20Technical%20Standards%20for%20E-voting_2004_EN.pdf)
[voting_2004_EN.pdf.](http://www.eods.eu/library/CoE_Recommentaion%20on%20Legal,%20Operational%20and%20Technical%20Standards%20for%20E-voting_2004_EN.pdf)

[4] Voting System Standards Volume I, Federal Election Commission, USA. April
[2002. https://www.eac.gov/sites/default/files/eac_assets/1/28/Voting_System_](https://www.eac.gov/sites/default/files/eac_assets/1/28/Voting_System_Standards_Volume_I.pdf)
[Standards_Volume_I.pdf.](https://www.eac.gov/sites/default/files/eac_assets/1/28/Voting_System_Standards_Volume_I.pdf)

[5] V. Buterin, Moving beyond coin voting governance, August, 2021. Accessed on:
[October 1, 2021. Available: https://vitalik.ca/general/2021/08/16/voting3.html.](https://vitalik.ca/general/2021/08/16/voting3.html)

[6] Wharton Cryptogovernance Workshop. Accessed on: October 19, 2021. Available:

[https://cryptogov.net.](https://cryptogov.net)

[7] B. S. Srinivasan and L. Lee, Quantifying Decentralization, news.earn.com, July, 28,
[2017. Accessed on: October 3, 2021. Available: https://news.earn.com/quantifying-](https://news.earn.com/quantifying-decentralization-e39db233c28e)
[decentralization-e39db233c28e.](https://news.earn.com/quantifying-decentralization-e39db233c28e)

[8] D. Salman, Governance, Polkadot Wiki, September 17, 2021. Accessed on: October
[1, 2021. Available: https://wiki.polkadot.network/docs/learn-governance.](https://wiki.polkadot.network/docs/learn-governance)

[9] Tezos Foundation, The Voting Process, Tezos Documentation, July 16, 2021.
[Accessed on: October 2, 2021. Available: https://gitlab.com/tezos/tezos/-/blob/](https://gitlab.com/tezos/tezos/-/blob/master/docs/010/voting.rst)
[master/docs/010/voting.rst.](https://gitlab.com/tezos/tezos/-/blob/master/docs/010/voting.rst)

[10] L. Dashjr, BIP Process, github.com, February, 4, 2016. Accessed on: October 14,
[2021. Available: https://github.com/bitcoin/bips/blob/master/bip-0002.mediawiki.](https://github.com/bitcoin/bips/blob/master/bip-0002.mediawiki)

[11] J. Schnelli et al., Contributing to Bitcoin Core, github.com, September, 26, 2015.
[Accessed on: October 14, 2021. Available: https://github.com/bitcoin/bitcoin/blob/](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md)
[master/CONTRIBUTING.md.](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md)

[12] P. Wuille, P. Todd, G Maxwell, and R. Russell, Version bits with timeout and
delay, github.com, October, 4, 2015. Accessed on: October 14, 2021. Available:
[https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki.](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)



72


SoK: Blockchain Governance AFT ’22, September 19–21, 2022, Cambridge, MA, USA




[13] V. Buterin, “A Next-Generation Smart Contract and Decentralized Application Platform", github.com, 2013. Accessed on: November 15, 2021. Available:
https://ethereum.org/en/whitepaper/.

[14] M. Becze, H. Jameson, et al., “EIP-1: EIP Purpose and Guidelines," Ethereum
Improvement Proposals, no. 1, October 2015. Accessed on: November 15, 2021.

[Online serial]. Available: https://eips.ethereum.org/EIPS/eip-1.

[15] “ _Tezos Docs_ ", September 9, 2016. Accessed on: October 23, 2021. Available:
https://gitlab.com/tezos/tezos/-/tree/master/docs.

[16] “Decred Documentation", April 26, 2016. Accessed on: November 16, 2021. Available: https://github.com/decred/dcrdocs.

[17] “Decred Change Proposals", May 6, 2017. Accessed on: November 21, 2021. Available: https://github.com/decred/dcps.

[18] R. Leshner, G. Hayes, “Compound: The Money Market Protocol", com[pound.finance, 2019. Accessed on: November 16, 2021. Available: https://](https://compound.finance/documents/Compound.Whitepaper.pdf)
[compound.finance/documents/Compound.Whitepaper.pdf.](https://compound.finance/documents/Compound.Whitepaper.pdf)

[[19] Coinbase Statistics on COMP, Accessed on: December 1, 2021. Available: https:](https://coinmarketcap.com/currencies/compound/)
[//coinmarketcap.com/currencies/compound/.](https://coinmarketcap.com/currencies/compound/)

[20] The Maker Protocol: MakerDAO’s Multi-Collateral Dai (MCD) System. Accessed

[on: November 16, 2021. Available: https://makerdao.com/en/whitepaper.](https://makerdao.com/en/whitepaper)

[21] Project Catalyst Community website. Accessed on: December 15, 2021. Available:

[https://cardanocataly.st.](https://cardanocataly.st)

[22] Kriss Baird, Introducing the Catalyst Circle. Accessed on: December 12, 2021.
[Available: https://iohk.io/en/blog/posts/2021/07/08/introducing-the-catalyst-](https://iohk.io/en/blog/posts/2021/07/08/introducing-the-catalyst-circle/)
[circle/.](https://iohk.io/en/blog/posts/2021/07/08/introducing-the-catalyst-circle/)

[23] Allen, D. W., and Berg, C. Blockchain governance: What we can learn from
the economics of corporate governance. _Allen, DWE and Berg, C (Forthcom-_
_ing)‘Blockchain Governance: What can we Learn from the Economics of Corporate_
_Governance_ (2020).

[24] Alwen, J., Ostrovsky, R., Zhou, H., and Zikas, V. Incoercible multi-party
computation and universally composable receipt-free voting. In _Advances in_
_Cryptology - CRYPTO 2015 - 35th Annual Cryptology Conference, Santa Barbara, CA,_
_USA, August 16-20, 2015, Proceedings, Part II_ (2015), R. Gennaro and M. Robshaw,
Eds., vol. 9216 of _Lecture Notes in Computer Science_, Springer, pp. 763–780.

[25] Anshelevich, E., Filos-Ratsikas, A., Shah, N., and Voudouris, A. A. Distortion in social choice problems: The first 15 years and beyond. _arXiv preprint_
_arXiv:2103.00911_ (2021).

[26] Arrow, K. J. A difficulty in the concept of social welfare. _Journal of political_
_economy 58_, 4 (1950), 328–346.

[27] Aziz, H., and Shah, N. Participatory budgeting: Models and approaches, 2020.

[28] Balinski, M., and Laraki, R. Majority judgment. _Cambridge/Mass_ (2011).

[29] Bartholdi, J. J., and Orlin, J. B. Single transferable vote resists strategic voting.
_Social Choice and Welfare 8_, 4 (1991), 341–354.

[30] Beck, R., Müller-Bloch, C., and King, J. L. Governance in the blockchain
economy: A framework and research agenda. _Journal of the Association for_
_Information Systems 19_, 10 (2018), 1.

[31] Benade, G., Nath, S., Procaccia, A. D., and Shah, N. Preference elicitation for
participatory budgeting. _Management Science 67_, 5 (2021), 2813–2827.

[32] Benaloh, J. Simple verifiable elections. In _2006 USENIX/ACCURATE Electronic_
_Voting Technology Workshop, EVT’06, Vancouver, BC, Canada, August 1, 2006_ (2006),
D. S. Wallach and R. L. Rivest, Eds., USENIX Association.

[33] Benaloh, J. C., and Tuinstra, D. Receipt-free secret-ballot elections (extended
abstract). In _Proceedings of the Twenty-Sixth Annual ACM Symposium on Theory_

_of Computing, 23-25 May 1994, Montréal, Québec, Canada_ (1994), F. T. Leighton
and M. T. Goodrich, Eds., ACM, pp. 544–553.

[34] Bethencourt, J., Shi, E., and Song, D. Signatures of reputation. In _Financial_
_Cryptography and Data Security, 14th International Conference, FC 2010, Tenerife,_
_Canary Islands, Spain, January 25-28, 2010, Revised Selected Papers_ (2010), R. Sion,
Ed., vol. 6052 of _Lecture Notes in Computer Science_, Springer, pp. 400–407.

[35] Brandt, F., Conitzer, V., and Endriss, U. Computational social choice. _Multia-_
_gent systems_ (2012), 213–283.

[36] Brill, M., Freeman, R., Janson, S., and Lackner, M. Phragmén’s voting methods
and justified representation. In _Proceedings of the AAAI Conference on Artificial_
_Intelligence_ (2017), vol. 31.

[37] Buterin, V., Hitzig, Z., and Weyl, E. G. A flexible design for funding public
goods. _Management Science 65_, 11 (2019), 5171–5187.

[38] Cevallos, A., and Stewart, A. A verifiably secure and proportional committee
election rule. In _Proceedings of the 3rd ACM Conference on Advances in Financial_
_Technologies_ (2021), pp. 29–42.

[39] Cohen, J. D., and Fischer, M. J. A robust and verifiable cryptographically secure
election scheme (extended abstract). In _26th Annual Symposium on Foundations_

_of Computer Science, Portland, Oregon, USA, 21-23 October 1985_ (1985), IEEE
Computer Society, pp. 372–382.

[40] Cortier, V., Galindo, D., Küsters, R., Mueller, J., and Truderung, T. Sok:
Verifiability notions for e-voting protocols. In _2016 IEEE Symposium on Security_
_and Privacy (SP)_ (2016), IEEE, pp. 779–798.

[41] Cuvelier, E., Pereira, O., and Peters, T. Election verifiability or ballot privacy:
Do we need to choose? In _European Symposium on Research in Computer Security_
(2013), Springer, pp. 481–498.




[42] De Filippi, P., and McMullen, G. Governance of blockchain systems: Governance of and by distributed infrastructure.

[43] Dykstra, C. A. The quest for responsibility. _American Political Science Review_
_33_, 1 (1939), 1–25.

[44] Gersbach, H., Mamageishvili, A., and Schneider, M. Vote delegation and
misbehavior. _arXiv preprint arXiv:2102.08823_ (2021).

[45] Gharadaghy, R., and Volkamer, M. Verifiability in electronic votingexplanations for non security experts. In _4th International Conference on Electronic_
_Voting 2010_ (2010), Gesellschaft für Informatik eV.

[46] Gibbard, A. Manipulation of voting schemes: a general result. _Econometrica:_
_journal of the Econometric Society_ (1973), 587–601.

[47] Grant, R. W., and Keohane, R. O. Accountability and abuses of power in world
politics. _American political science review 99_, 1 (2005), 29–43.

[48] Howell, G. One man, one vote. Manchester Selected Pamphlets. JSTOR 60239578,
1880.

[49] Hsieh, Y.-Y., Vergne, J.-P. J., and Wang, S. The internal and external governance

   - f blockchain-based organizations: Evidence from cryptocurrencies. 48–68.

[50] Juels, A., Catalano, D., and Jakobsson, M. Coercion-resistant electronic
elections. In _Towards Trustworthy Elections_ . Springer, 2010, pp. 37–63.

[51] Khan, N., Ahmad, T., Patel, A., and State, R. Blockchain governance: An

   - verview and prediction of optimal strategies using nash equilibrium. _arXiv_
_preprint arXiv:2003.09241_ (2020).

[52] Kiayias, A., and Lazos, P. Sok: Blockchain governance. _arXiv preprint_
_arXiv:2201.07188_ (2022).

[53] Kiayias, A., Zacharias, T., and Zhang, B. Ceremonies for end-to-end verifiable
elections. In _Public-Key Cryptography - PKC 2017 - 20th IACR International_
_Conference on Practice and Theory in Public-Key Cryptography, Amsterdam, The_
_Netherlands, March 28-31, 2017, Proceedings, Part II_ (2017), S. Fehr, Ed., vol. 10175

   - f _Lecture Notes in Computer Science_, Springer, pp. 305–334.

[54] Kluiving, B., de Vries, A., Vrijbergen, P., Boixel, A., and Endriss, U. Analysing
irresolute multiwinner voting rules with approval ballots via sat solving. In _ECAI_
_2020_ . IOS Press, 2020, pp. 131–138.

[55] Lalley, S. P., and Weyl, E. G. Quadratic voting: How mechanism design can
radicalize democracy. 33–37.

[56] Liu, Y., Lu, Q., Zhu, L., Paik, H.-Y., and Staples, M. A systematic literature
review on blockchain governance. _arXiv preprint arXiv:2105.05460_ (2021).

[57] Nakamoto, S. Bitcoin: A peer-to-peer electronic cash system.

[58] Panagopoulos, C. Extrinsic rewards, intrinsic motivation and voting. _The_
_Journal of Politics 75_, 1 (2013), 266–280.

[59] Pelt, R. v., Jansen, S., Baars, D., and Overbeek, S. Defining blockchain governance: a framework for analysis and comparison. _Information Systems Manage-_
_ment 38_, 1 (2021), 21–41.

[60] Prato, C., and Wolton, S. The voters’ curses: why we need goldilocks voters.
_American Journal of Political Science 60_, 3 (2016), 726–737.

[61] Prato, C., and Wolton, S. Rational ignorance, populism, and reform. _European_
_Journal of Political Economy 55_ (2018), 119–135.

[62] Rivest, R. L., and Shen, E. An optimal single-winner preferential voting system
based on game theory. In _Proc. of 3rd International Workshop on Computational_
_Social Choice_ (2010), Citeseer, pp. 399–410.

[63] Sacco, D. F., Bruton, S. V., Brown, M., and Medlin, M. M. Skin in the game:
Personal accountability and journal peer review. _Journal of Empirical Research_

_on Human Research Ethics 15_, 4 (2020), 330–338. PMID: 32425095.

[64] Satterthwaite, M. A. Strategy-proofness and arrow’s conditions: Existence
and correspondence theorems for voting procedures and social welfare functions.
_Journal of economic theory 10_, 2 (1975), 187–217.

[65] Shineman, V. A. If you mobilize them, they will become informed: experimental
evidence that information acquisition is endogenous to costs and incentives to
participate. _British Journal of Political Science 48_, 1 (2018), 189–211.

[66] Siddarth, D., Ivliev, S., Siri, S., and Berman, P. Who watches the watchmen?
a review of subjective approaches for sybil-resistance in proof of personhood
protocols. _Frontiers in Blockchain 3_ (2020), 46.

[67] Taylor, B. R. The psychological foundations of rational ignorance: biased heuristics and decision costs. _Constitutional Political Economy 31_, 1 (2020), 70–88.

[68] Venugopalan, S., and Homoliak, I. Always on voting: A framework for repetitive voting on the blockchain. _arXiv preprint arXiv:2107.10571_ (2021).

[69] von Ahn, L., Blum, M., Hopper, N. J., and Langford, J. CAPTCHA: using hard AI
problems for security. In _Advances in Cryptology - EUROCRYPT 2003, International_
_Conference on the Theory and Applications of Cryptographic Techniques, Warsaw,_
_Poland, May 4-8, 2003, Proceedings_ (2003), E. Biham, Ed., vol. 2656 of _Lecture Notes_
_in Computer Science_, Springer, pp. 294–311.

[70] Zhang, B., Oliynykov, R., and Balogun, H. A treasury system for cryptocurrencies: Enabling better collaborative intelligence. In _The Network and Distributed_
_System Security Symposium 2019_ (2019).

[71] Zhang, Y., and van der Schaar, M. Reputation-based incentive protocols in
crowdsourcing applications. In _2012 Proceedings IEEE INFOCOM_ (2012), pp. 2140–
2148.



73


