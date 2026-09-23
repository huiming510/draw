# 异兽装饰壁画 Skill

工作区 Skill：[mythic-beast-mural](.agents/skills/mythic-beast-mural/SKILL.md)。内容包含认可的穷奇原始参考图、画风规范、角色档案、提示词模板与分阶段生图流程。

## 人工验证

当前顺序：先确定整体画风，再定制角色与背景细节。05 烛龙、06 毕方两张背景修订图作为[暂存探索稿](output/mythic-beast-mural/2026-09-23-background-test/REVIEW.md)保留，暂不继续细化。

历史方向：08版形态与10版中轴昼夜均被用户否定。[09版山谷场景](output/mythic-beast-mural/2026-09-23-zhulong-scene/REVIEW.md)和其他探索保留供追溯。

当前最新候选：[15 烛龙：环境符号化的角色图版](output/mythic-beast-mural/2026-09-23-zhulong-symbolic/15-zhulong-symbolic-plate.png)。用户澄清需要角色档案画，其他元素抽象化、符号化；本轮放大盘蛇，将岩岸、水面凝练为平面色块与水纹，保留睁眼蛇首和闭眼人面倒影。[完整提示词与检查记录](output/mythic-beast-mural/2026-09-23-zhulong-symbolic/REVIEW.md)，待人工判断。

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
