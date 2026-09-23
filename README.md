# 异兽装饰壁画 Skill

工作区 Skill：[mythic-beast-mural](.agents/skills/mythic-beast-mural/SKILL.md)。内容包含认可的穷奇原始参考图、画风规范、角色档案、提示词模板与分阶段生图流程。

## 人工验证

当前顺序：先确定整体画风，再定制角色与背景细节。05 烛龙、06 毕方两张背景修订图作为[暂存探索稿](output/mythic-beast-mural/2026-09-23-background-test/REVIEW.md)保留，暂不继续细化。

历史方向：08版形态与10版中轴昼夜均被用户否定。[09版山谷场景](output/mythic-beast-mural/2026-09-23-zhulong-scene/REVIEW.md)和其他探索保留供追溯。

当前最新候选：[23 烛龙：上下中轴构图](output/mythic-beast-mural/2026-09-23-zhulong-vertical-axis/23-zhulong-vertical-axis.png)。按用户最新指令改为竖向图版，上方盘蛇的睁眼蛇首与下方闭眼人面倒影同轴，环境保持抽象水岩纹样。[提示词、参考稿与检查记录](output/mythic-beast-mural/2026-09-23-zhulong-vertical-axis/REVIEW.md)，待人工判断。

[20／21丰润与受力修订](output/mythic-beast-mural/2026-09-23-zhulong-weight/REVIEW.md)保留追溯；20被用户评价仍不自然，21尚未获认可，22尾段修正草案未执行即转向上下中轴。

[19连接修订与结构参考](output/mythic-beast-mural/2026-09-23-zhulong-continuity/REVIEW.md)保留追溯，用户反馈体态尚不够丰润、垂落不够自然。

[15环境符号化稿](output/mythic-beast-mural/2026-09-23-zhulong-symbolic/REVIEW.md)保留为原姿态参考，身体连续性被用户明确指出需修。16螺旋盘法不采用；17文字修正失败，18未能确认修复，均保留追溯。

[13／14场景探索](output/mythic-beast-mural/2026-09-23-zhulong-narrative/REVIEW.md)源于Agent对上一句反馈的误解，未达成档案画目标；[11／12倒影探索](output/mythic-beast-mural/2026-09-23-zhulong-reflection/REVIEW.md)也保留供追溯。

- [打开本地验收页](output/mythic-beast-mural/2026-09-23-transfer-test/review.html)：穷奇基准、烛龙和毕方黑白／彩色对照，可放大、填写与导出意见。
- [检查记录与完整提示词入口](output/mythic-beast-mural/2026-09-23-transfer-test/REVIEW.md)。
- [逐次生成记录](output/mythic-beast-mural/2026-09-23-transfer-test/manifest.json)：5 次内置生图调用、输入图角色、完整实际 prompt、输出哈希和尺寸。

新图全部待用户验证。已完成 2 个角色各一张黑白稿与彩稿，毕方另保留一次取景修正前的版本。优先确认烛龙人面的气质、毕方羽冠的华丽程度与整体同系列感。

## 调用示例

```text
$mythic-beast-mural 为白泽设计同系列黑白结构稿，先核实采用的文献形态。

$mythic-beast-mural 只为我已认可的结构稿上色，保留轮廓和主要纹样。
```

反馈可以直接写：`图号 + 保留／修改／淘汰 + 具体部位或感觉`。在用户明确认可前，测试图不会取代穷奇基准。
