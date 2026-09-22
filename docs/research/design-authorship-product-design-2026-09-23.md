# design-authorship：产品设计流程与前端美学升级调研

日期：2026-09-23（Australia/Melbourne）。

来源与状态：本文件直接响应本次用户提出的“合并现有内容、建立升级分支、深度调研”请求，是本轮调研及升级建议的唯一入口。第 8 节是待确认的实施建议，尚未修改 skill 本体；后续若拆分实施计划，应在子文档开头声明衍生自本文件及其具体章节。

本地基线：`main` 已整合至 `4b886a2db251c54f071676a100e5353dde3c6fb4`。调研分支为 `codex/design-authorship-product-design`。当前版本为 `design-authorship v0.1.2`、`human-ai-governance v0.7.7`、`scaffold-research-task v0.1.2`。

## 1. 结论与证据范围

建议升级现有 `design-authorship`，把它从“设计原则、视觉指导和结果检查”进一步变成能够引导 **Product Design Process（产品设计流程）** 的 skill：使用情境 → 任务与信息结构 → 构图探索 → 视觉方向 → 可操作原型 → 实现 → 任务与视觉验收。前面的决定应当支持后面的决定；发现结构问题时允许返回修改。

用户描述的“矩形堆砌、信息平铺、僵硬”，值得优先调查的是：页面是否把功能目录直接变成了一组等权组件，省略了信息优先级、整体布局和真实任务的推敲。**这是有依据的工作假设，尚未证明是用户过去页面的实际生成原因。** 本轮没有取得那些页面的完整任务记录、skill 加载记录和渲染结果，也没有运行旧版与候选版的页面生成对照。

现有 skill 已经反对机械套用卡片、颜色和字体，也要求真实内容、交互状态及渲染检查。继续叠加“禁止卡片”“必须不对称”等限制，收益可能有限。真正需要补强的是中间的设计决策与实际产物评估。

本轮采用三类证据：

| 证据 | 可以支持的判断 | 不能推出的判断 |
| --- | --- | --- |
| 团队手册、官方方法、工具文档 | 某团队如何工作、某工具能够传递或验证什么 | 全行业采用率、工具效果保证 |
| 公开设计 skill、开发者实践文章与工程实验 | 可检查的工作方式、作者报告的经验与限制 | 普适美学标准、跨模型稳定增益 |
| 当前仓库源码与测试 | skill 写了什么、测试实际检查什么 | 每次任务都加载并执行了这些规则、页面已经更好看 |

用户提供的 GPT Pro 总结作为问题与建议的输入，未被当作独立外部证据。外部来源均于本轮联网核对，访问日期统一为 2026-09-23。选择的是可追溯的一手资料，没有用搜索排名、星标数量或营销文案推导社区占比。

## 2. “AI 味”应拆成可以诊断的现象

下表是本报告的诊断框架，供后续检查真实页面；不表示已经在用户项目中逐项观察到这些问题。

| 表面现象 | 要检查的设计决定 | 可能的修正 |
| --- | --- | --- |
| 所有模块都是相同大小的卡片 | 不同信息是否确实同等重要；边界是否对应独立对象 | 重新分配主次面积，将连续任务放回共同工作区 |
| 内容齐全但没有重点 | 用户进入页面后首先要判断什么、执行什么 | 建立主工作区、主要信息和辅助上下文 |
| 表格、图表、说明彼此分割 | 哪些值需要一起看；是否需要记住上一屏的信息 | 对齐比较、共享坐标、详情联动、减少不必要跳转 |
| 换颜色后仍然像模板 | 整体构图、内容密度、图文关系是否改变 | 根据具体任务重新选择空间组织方式 |
| 概念图很漂亮，成品失去特点 | 图中哪些关系是必须保留的；真实内容是否容得下 | 把构图提炼成规则，先用长文本和密集数据验证 |
| 默认页面好看，点击后混乱 | 展开、选择、失败、返回时的状态和焦点 | 检查操作后的页面及任务恢复过程 |
| 为了特别而增加曲线和动画 | 元素是否承担内容、品牌或反馈作用 | 保留有作用的表达，降低无关视觉竞争 |

OpenAI 关于 GPT-5.4 的前端文章将欠明确的要求与模型回落到高频模式联系起来，建议补充设计约束、视觉参照与内容结构。这是供应商针对相关模型的指导，可支持上述调查方向；它没有证明当前模型在用户任务中的具体成因。[OpenAI 前端设计文章](https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4)

## 3. 对用户贴文的核验与修正

### 3.1 成熟流程确实把设计放在实现之前，也延续到实现之后

GitLab 的流程从用户、问题与目的出发，读取研究、设计用户流程，并让工程师早期参与可行性讨论。探索之后要收敛为明确方案；该手册通常希望最终提出一个经过验证的方案。这支持“先探索再选择”，不支持每次都提交三套完整方案。[GitLab Product Designer Workflow](https://handbook.gitlab.com/handbook/upstream-studios/product-design/workflow/)

GOV.UK 的 Discovery（探索阶段）关注用户情境、限制和成功标准；Alpha（原型探索阶段）用于检验关键假设。原型可以是纸面，也可以是运行中的代码，完成度应由待解决的问题决定。原型代码不能直接被当作生产质量代码。[Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)、[Alpha](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)、[Making prototypes](https://www.gov.uk/service-manual/design/making-prototypes)

Double Diamond（双钻模型）强调展开、收敛和反复学习，允许早期制作与测试，也允许返回前面的阶段。贴文的八阶段是合理的组合建议，不能写成每个小任务都必须依次完成八份文档的规定。[Design Council](https://www.designcouncil.org.uk/resources/framework-for-innovation/)

### 3.2 布局与视觉语言可以并行探索，但解决不同问题

Style Tile（风格板）用字体、颜色和局部界面元素表达视觉语言，本身不规定完整布局。它可以配合信息结构和线框使用。三种配色只能帮助比较色彩方向，不能代替结构方案比较。[Samantha Warren 原文](https://alistapart.com/article/style-tiles-and-how-they-work/)、[Style Tiles 原始网站](https://styletil.es/)

因此，本报告建议把不确定性拆开：不知道“信息如何组织”，先画布局与流程；不知道“应有什么视觉气质”，比较风格板或概念图；不知道“操作是否顺手”，制作能执行关键任务的原型。这是面向本仓库的组合建议。

### 3.3 三种动线需要不同证据

| 层次 | 应当回答的问题 | 证据 |
| --- | --- | --- |
| Task Flow（任务流程） | 怎样从目标出发，经过选择、操作与恢复到达结果 | 执行完整任务，检查分支和错误恢复 |
| Visual Hierarchy（视觉层级） | 哪些内容被设计为先看到，主次是否清楚 | 渲染评审；真实观察才能说明用户实际看了什么 |
| Interaction Ergonomics（操作便利性） | 点击、触摸、键盘焦点及反复操作是否顺手 | 实际操作、焦点检查、目标尺寸与上下文稳定性 |

NN/G 说明 F 形扫描只是部分阅读情境中的模式，涉及内容区，不能套用为所有应用的导航规律。画出的注意力箭头只能表达设计意图，不能充当 Eye Tracking（眼动追踪）结果。[NN/G 原始研究说明](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)

WCAG（网页内容无障碍指南）2.2 的目标尺寸最低准则有 `24 × 24 CSS px` 及明确例外，不能简化为所有控件都必须固定这个尺寸。焦点顺序需要保留意义与可操作性，也不要求与视觉顺序逐点完全一致。[Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)、[Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order)

### 3.4 AI 可以加速设计，不能提供虚构的用户验证

GitLab 的 AI 指导支持多方向探索、错误状态、界面文案、线框和功能原型，同时要求审查生成结果；假设性用户角色需明确标记并由真实用户研究检验。日期上，页面显示内容更新于 2026-06-15，页脚修改时间为 2026-06-18，贴文中的前一个日期存在，但不应称为最后修改日期。[GitLab AI usage](https://handbook.gitlab.com/handbook/upstream-studios/how-we-work/ai-usage/)

OpenAI 当前前端提示页面明确区分工作型应用与游戏等表达性界面：前者侧重扫描、比较和重复操作。该页注明面向 GPT-5.5，不能把其中全部圆角、字体、配色等具体偏好升级为当前所有模型的普遍设计标准。[OpenAI Frontend prompt instructions](https://developers.openai.com/api/docs/guides/frontend-prompt)

## 4. 开发者与开源社区中可观察到的做法

以下是公开资料中反复出现的模式，属于定性归纳，不是全行业采用率排名。

| 做法 | 一手实例 | 对本次升级有用的部分 | 适用边界 |
| --- | --- | --- | --- |
| 先给产品情境，再生成页面 | [Vercel：How to prompt v0](https://vercel.com/blog/how-to-prompt-v0) | 明确页面数据与操作、使用者当下情境和约束 | 供应商示例不等于受控效果证明；文中也有合理的卡片布局 |
| 把设计判断写成可复用 skill | [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 内容与任务决定方向，编码前审视方案，之后看截图批评 | 具体审美偏好需服从用户与既有系统 |
| 把模糊的“美化”拆成具体动作 | [Impeccable](https://github.com/pbakaus/impeccable) | 分开诊断布局、文字、颜色、状态与细节 | 自动检测只能发现它定义的问题，不能裁决整体美感 |
| 区分产品事实与视觉决定 | [Designing with Impeccable](https://impeccable.style/designing/) | 复用上下文，支持概念图起步或直接做代码原型 | 沿用现有项目文档即可，无需强制增加相同文件名 |
| 给生成器提供真实设计系统 | [Vercel：AI-powered prototyping with design systems](https://vercel.com/blog/ai-powered-prototyping-with-design-systems) | 输入 Design Tokens（设计令牌）、组件及产品专用组合 | 一致性不能独自解决信息主次和整页构图 |
| 用可修改的组件作实现材料 | [shadcn/ui](https://ui.shadcn.com/docs) | 开放源码、组合接口及分发机制，便于适配产品 | 组件库不是完整页面的设计答案 |
| 用结构化设计数据连接代码 | [Figma MCP](https://developers.figma.com/docs/figma-mcp-server/structure-figma-file/) | 组件、变量、语义命名、布局与行为注释一起传递 | 仍需维护映射并检验实际页面 |
| 展示可运行的设计变体 | [Emil Kowalski skills](https://github.com/emilkowalski/skills) | 通过不同实现对照来讨论细节与选择方向 | 代表作者实践，不能证明普适偏好 |
| 生成与独立评审分工 | [Anthropic 工程实验](https://www.anthropic.com/engineering/harness-design-long-running-apps) | 评审者查看真实页面，给出具体问题，再迭代 | 评审标准仍需人工校准；多轮生成有明显成本 |

### 4.1 一份“反 AI 模板”也可能变成模板

本轮读到的 Anthropic skill 已把奶油底配衬线字、暗底配亮色、报纸式细线布局及传统 SaaS 卡片列为容易重复出现的方向，同时承认这些方向可适用于具体要求。这说明“避开一种视觉配方”不足以保证设计具有辨识度；它不构成这些风格流行程度的统计证据。[当前公开源码](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

本报告建议保留的规则是：**检查视觉选择有没有内容、任务或品牌依据，避免无理由的重复。** 不建议把禁用特定字体、紫色、圆角、卡片、对称布局写成通用要求，也不建议规定每页必须包含多少种形状或动画。

### 4.2 组件系统与产品设计承担不同责任

设计系统帮助重复行为保持一致。页面结构仍然需要回答“哪些信息必须一起看、哪些操作反复发生、什么可以晚一点出现”。把“采用 shadcn/ui”直接当成布局方向，会留下这部分决定未被处理的风险；这个判断是本报告对组件文档与工作流的综合分析。

Figma 的 Code Connect 可以提供组件与实现的映射，但 CLI 与 UI 建立的映射信息并不完全相同，后者默认不包含完整实现示例。截图、设计文件和代码组件可以互补，任何一个都不能单独保证成品忠实或交互正确。[Code Connect integration](https://developers.figma.com/docs/figma-mcp-server/code-connect-integration/)

### 4.3 独立评审有价值，但不要无限循环打分

Anthropic 的工程作者报告了生成者与评审者分离的实验，也指出评审措辞会使视觉风格收敛，并且自己有时更喜欢中间版本。它支持使用独立、具体、经过校准的批评，不能证明评分越来越高就代表用户体验越来越好。[工程实验及限制](https://www.anthropic.com/engineering/harness-design-long-running-apps)

对本仓库，比较实用的方式是有限轮次的“查看产物 → 记录可定位的问题 → 修正原因 → 复查”，达到已约定目标便停止。不要把审美数字分数设为发布闸门，也不要以代理模拟用户的评语冒充真实 Usability Testing（可用性测试）。

### 4.4 论坛中的亲历做法与分歧

2026-02-19 的 Hacker News 讨论中，`embedding-shape` 描述先建立 Figma 参考、再让代理对照浏览器截图检查的做法；`rglover` 选择亲自完成 HTML/CSS 设计后委托实现细节；`Dollarland` 则报告结合 Claude、v0 与 shadcn/ui 并反复调整视觉。它们说明开发者采用多种分工方式，不能推出某一工具链最优。[截图对照实践](https://news.ycombinator.com/item?id=47074302)、[手工设计起步](https://news.ycombinator.com/item?id=47075075)、[组件库配合迭代](https://news.ycombinator.com/item?id=47080578)

2026-05-02 的另一场讨论围绕 shadcn 默认外观展开：有参与者不希望自己的作品被看作 AI 生成，另有参与者强调组件本来就可修改，也有人认为只改配色与圆角仍保留了模板结构。这些是参与者的亲历陈述和观点，未独立验证其项目效果。[讨论入口](https://news.ycombinator.com/item?id=47985052)、[可修改组件的观点](https://news.ycombinator.com/item?id=47985163)、[表层修改的局限](https://news.ycombinator.com/item?id=47985939)

本报告从中采纳的启示是保留可复用行为，同时认真设计整页结构。不能仅凭用了某个组件库便断定 AI 作者身份，也不能把截图相似度等同于可用性。这两个自选样本只提供实践线索，不提供社区代表性。

## 5. 当前 skill 的实际缺口

核对基线为 `4b886a2`，下表链接指向当前仓库文件。现有优点应保留，升级应增强实际决策能力。

| 已有能力 | 缺口 | 建议补充位置 |
| --- | --- | --- |
| audience、任务、情绪与限制 | 使用频率、熟练度、情境、出错后果及成功表现还不够明确 | [intent-and-reference.md](../../skills/design-authorship/references/intent-and-reference.md) |
| 内容关系到形式的映射 | 缺少“对象、属性、操作、关系和状态”到 Information Architecture（信息架构）的推导 | 增加一个按需读取的产品结构参考文件 |
| 概念图方向校准 | 在真实任务与代表性内容结构形成前，就可能进入概念图环节 | [SKILL.md](../../skills/design-authorship/SKILL.md)、[concept-image-calibration.md](../../skills/design-authorship/references/concept-image-calibration.md) |
| 结构不同的候选方向 | 没明确要求用相同内容比较，也没明确区分线框占位与可见容器 | [intent-and-reference.md](../../skills/design-authorship/references/intent-and-reference.md) |
| 单个容器的必要性检查 | 多个各自合理的卡片，仍可能共同造成整屏碎片化 | [content-to-form.md](../../skills/design-authorship/references/content-to-form.md) |
| 窗口与交互状态检查 | 任务路径、预期注意力、操作焦点容易混在一起 | [ui-interaction.md](../../skills/design-authorship/references/ui-interaction.md) |
| 先看实际产物再看设计解释 | 问题还需追溯到信息结构、任务流程、构图或局部细节 | [critique-and-verification.md](../../skills/design-authorship/references/critique-and-verification.md) |
| 保存长久设计决策 | 必须保留的设计意图与可调整的示例细节未充分区分 | [project-design-context.md](../../skills/design-authorship/references/project-design-context.md) |
| 测试场景与包检查 | 当前自动测试主要检验 YAML 结构、文件、版本及约定文本，没有生成并评价页面 | [test_evaluation_contract.py](../../tests/design-authorship/test_evaluation_contract.py)、[test_package.py](../../tests/design-authorship/test_package.py) |

这解释了为什么“规则已经写了”与“实际输出更好”之间仍有距离。还需在后续真实任务中确认 skill 是否被加载、是否走了合适路线，以及设计选择是否保留到了最终页面。

## 6. 建议的工作流程：按问题选择深度

### 6.1 先建立最小设计依据

对新界面或实质改版，保留六项足以改变设计的内容：使用者与情境、主要目标、代表性真实内容、核心对象和操作、成功表现、不可改变的限制。区分已知事实、暂时假设、已确认决定。已有材料足够时直接复用，不要求用户重新填写问卷。

例如，“内部人员每天比较多笔记录”会影响密度、排序、同时显示的字段和连续操作；“访客偶尔完成一次申请”会影响说明、分步反馈、保存和错误恢复。它们无法仅由“专业、简洁”推导出来。

### 6.2 从任务推导结构

用一条主任务链表达“从哪里开始、要做什么判断、操作什么对象、看到什么反馈、如何完成或恢复”。必要时补充 Wireflow（线框流程图），把页面变化和操作连接起来。

先决定哪些信息应同时出现、哪些内容属于对象属性、哪些是状态、哪些需要独立导航，再选择模块。对小修复，复用既有任务结构即可。

### 6.3 结构与视觉分别探索，然后收敛

有未解决的实质布局选择时，用同一批关键内容比较不同组织方式。可以用线框、简短示意或运行中的低完成度页面。比较主工作区、辅助上下文、同时比较能力、信息展开顺序和空间比例，不用换颜色充当结构探索。

视觉语言通过真实品牌材料、风格板、参考分析或概念图讨论。选择之后记录为什么适合该任务。已经批准的方向继续执行；“新项目”本身不意味着必须重新选择固定数量的方案。

线框里的矩形只是空间占位。最终是否显示背景、边框、圆角，应由分组、操作、状态或品牌表达决定。

### 6.4 做一次整页构图检查

局部容器检查之外，增加整页问题：主工作区是否足够突出；相同面积是否暗示了错误的同等重要性；卡片边距是否压缩了比较空间；相关信息是否能共享基线；连续任务是否被割裂；视觉重复是否帮助学习。

需要记忆点时，把变化放到有意义的位置：字形与排版、主体图像、比例、路径、共同坐标、留白节奏、操作反馈。圆形和曲线可以表达身份、进度、连续性或品牌特征；不能为了“少一点矩形”随意加入。

### 6.5 把选定方向变成实现规则

在现有设计文档中保留必要规则：主要区域的比例与可伸缩方式、边界的使用理由、字体与图像的关系、窗口变窄时的信息优先级、关键状态和焦点恢复。另列允许自由调整的示例文字、局部间距等细节。

由构建工具完成代码和组件实现。选用什么框架、安装什么插件、如何部署仍服从项目已有约定，不由设计 skill 自动扩展。

### 6.6 分别验收任务、视觉与实现

任务检查关注能否完成、哪里需要记忆或往返、错误后能否继续。视觉检查关注重点、比例、辨识度与所选方向。实现检查关注真实内容、支持的窗口、键盘、状态和资源是否正常。

GitLab 的设计评审使用可运行环境，因为截图不能充分检查悬停、小窗口和无障碍问题。[GitLab Merge Request Reviews](https://handbook.gitlab.com/handbook/upstream-studios/product-design/workflow/mr-reviews/)

Storybook 的状态、交互与视觉测试分别提供不同证据。Visual Regression Testing（视觉回归测试）适合发现相对于已批准外观的变化，无法单独证明该外观有美感或任务有效。不强制每个原型引入 Storybook。[Storybook UI testing](https://storybook.js.org/docs/writing-tests)、[Visual Testing Handbook](https://storybook.js.org/tutorials/visual-testing-handbook)

## 7. 同一流程如何产生不同页面

以下为合成示例，用于说明设计推导；没有检查、评价或修改这些真实项目，也没有认定唯一正确布局。

| 示例任务 | 应优先表达的关系 | 值得比较的构图 | 需要检验的结果 |
| --- | --- | --- | --- |
| 客户提交材料 | 准备事项、步骤、缺项、结果 | 连续步骤与局部说明；单页分区与进度 | 能否知道下一步，失败后是否保留输入 |
| 内部人员处理案件 | 待办队列、当前对象、证据与操作 | 列表联动详情；工作区加辅助面板 | 能否连续处理，返回后是否丢失筛选与位置 |
| 研究者比较实验 | 对齐指标、差异、数据来源与状态 | 比较表与详情；共享坐标图与注释 | 能否直接比较，无需跨屏记忆数值 |
| 学习者完成练习 | 当前题、反馈、下一步 | 集中练习舞台；安静排版与局部陪伴角色 | 输入与反馈是否清楚，能否流畅进入下一题 |
| 浏览独立作品或商品 | 同级对象、图片、局部操作 | 有明确层级的卡片集合；列表与预览 | 卡片是否确实帮助浏览和选择 |

最后一种是必要的反例：合理卡片集合必须保留。否则升级可能只是把所有项目从同一种布局推向另一种布局。

## 8. 建议实施范围与验证办法

本节为待确认建议，尚未实施。不另建职责重叠的“美学/前端 skill”；保留 `design-authorship` 名称、UI/幻灯片/图示路由和按需读取参考文件的结构。若按本节完成实质能力增加，可考虑升级为 `v0.2.0`，最终版本在实现时确定。

### stage1.1 补充产品结构与原型选择

新增一个聚焦参考文件，建议命名 `references/product-structure.md`。内容只保留使用情境、对象与操作、信息结构、任务与状态、原型选择这些能改变决定的指引。入口增加路线，并让真实任务与内容结构先于依赖它们的概念探索。局部改动复用既有结构。

### stage1.2 加强构图与设计意图传递

更新现有方向、内容形式、概念图和设计上下文参考：同内容比较、整页容器检查、形状角色、核心设计意图与可变细节。保留已批准方向和已有授权，不增加固定审批次数或风格禁令。

### stage1.3 加强评审与真实行为验证

把问题修复指向原因：跨页记忆负担优先查信息结构；操作无法完成优先查流程与状态；主次不清查构图与视觉层级；局部不齐再查间距细节。补充三个验收维度和真实页面对照，明确自动包检查与设计效果的区别。

### stage1.4 同步与发布准备

更新测试输入、skill 版本、索引、变更记录和版本证据，运行仓库总验证及官方格式检查；保留对幻灯片、图示、小修复和已批准方向的回归覆盖。实际 push、tag、安装链接修改和下游迁移继续按仓库规则单独授权。

### 8.1 怎样判断升级有没有作用

建议先进行决策层检查，再做少量成对页面实验。以下是实验设计，尚未运行。

| 检查 | 输入与控制 | 看什么 | 不宣称什么 |
| --- | --- | --- | --- |
| 独立决策检查 | 旧版与候选版各收到相同原始需求，不提供期望答案 | 是否从任务推导结构、复用授权、选对原型、保留合理卡片 | 书面回答正确不等于成品更好 |
| 成对页面实验 | 同一模型设置、工具、真实内容样本、约束与相当执行预算 | 任务完成、信息比较、整体层级、参考意图是否落地 | 单次结果不代表稳定增益 |
| 盲化视觉比较 | 隐去版本标签，打乱左右顺序，保留相同窗口和状态 | 用户偏好及其可解释理由，独立评审定位问题 | 不把评审者个人偏好说成普遍真理 |
| 功能与无障碍检查 | 关键任务、长文本、密集数据、空/错误/展开后状态 | 是否因追求表现破坏可用性 | 通过有限检查不等于完整合规认证 |

首批页面建议选“密集比较工作区”“集中学习体验”“有真实品牌内容的说明页”，再用“合理卡片集合”“已批准设计的小修改”作防过度修正检查。若要声称稳定改善，应扩展任务并重复生成，而非只挑最好看的一对。

记录模型与设置、skill 内容身份、实际加载路线、输入内容、工具、耗时和修改轮次。将截图、可运行产物与执行证据留在合适的临时评估目录；仓库只保留简洁结论和可追溯信息，不提交生成运行日志或私有项目数据。

若候选版只多写了一份设计解释，成品仍然等权堆砌，应判定目标未达成。如果某个任务适合卡片，不应因为卡片数量多而扣分。如果新版大幅增加流程成本却没有可观察收益，应缩短或撤回相应规则。

## 9. 本轮完成状态

1. 保存并提交原有 31 个改动文件：`4b886a2`。
2. 将当前开发分支快进合并到本地 `main`，包含此前的研究 scaffold 更新；合并时其他本地分支均已被 `main` 包含。
3. 从该基线创建 `codex/design-authorship-product-design`。
4. 对现有内容完成仓库总验证：3 个 skill、9 组回归脚本；3 个 skill 的官方 `quick_validate.py` 均通过；差异空白检查通过。
5. 完成用户贴文核验、社区与工具实践调研、当前源码缺口审查及本文件的升级建议。尚未执行候选 skill 页面实验。

本轮没有 push、创建 tag、修改安装链接或迁移下游项目。研究分支中的本文件属于调研产物，skill 本体保持合并后的版本。

## 10. 可追溯来源补充

正文链接直接支持其所在段落。下面对容易变化的开源资料额外固定到本轮查询到的提交；其他网页仅记录访问日期，不编造缺失的版本号或更新时间。

| 来源 | 本轮确认的身份 | 固定证据 |
| --- | --- | --- |
| Anthropic skills | `main`：`34040c9c568585f6929bedeaad110ad08f079624` | [frontend-design 源码](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md) |
| Impeccable | `main`：`83c2c735777c68e30ea536ab9cc97f7843456945` | [权威入口 skill/SKILL.src.md](https://github.com/pbakaus/impeccable/blob/83c2c735777c68e30ea536ab9cc97f7843456945/skill/SKILL.src.md) |
| Impeccable 产品事实与视觉记录 | 同一提交中的维护源文件 | [init.md](https://github.com/pbakaus/impeccable/blob/83c2c735777c68e30ea536ab9cc97f7843456945/skill/reference/init.md)、[document.md](https://github.com/pbakaus/impeccable/blob/83c2c735777c68e30ea536ab9cc97f7843456945/skill/reference/document.md)、[new-work.md](https://github.com/pbakaus/impeccable/blob/83c2c735777c68e30ea536ab9cc97f7843456945/skill/reference/new-work.md) |

上述提交身份通过公开仓库的只读查询取得。本轮借鉴的是工作方法和决策依据，未将第三方 skill 代码或完整指令复制进本仓库，也未安装这些工具。
