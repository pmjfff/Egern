# Egern

自用 Egern 代理配置、规则与脚本合集。

## 📁 目录结构

```
├── Egern.yaml                        # 主配置文件
├── rule/                             # 规则文件（每日自动更新）
│   ├── Direct_Rule.rule              # 国内直连
│   ├── Proxy_Rule.rule               # 代理列表
│   └── Reject_Rule.rule              # 广告拦截/隐私
├── script/                           # 小组件脚本
│   ├── Cal_Widget.js                 # 万年历
│   ├── IPDashboard_Widget.js         # IP 信息仪表盘
│   ├── OilPrice_Widget.js            # 全国油价监控
│   ├── ServerPro_Widget.js           # 服务器 SSH 监控
│   ├── SpeedTest_Widget.js           # 网速测试
│   ├── Sub_Widget.js                 # 机场订阅流量监控
│   └── TestFlight_Widget.js          # TestFlight 监控
├── module/                           # 模块
│   └── TelegramRedirect_Module.module # Telegram 链接跳转
└── .github/workflows/                # 自动更新
    ├── update-rules.yml              # 工作流
    ├── Get_File.py                   # 拉取规则
    └── Merge_File.py                 # 合并去重
```

## 🔄 规则自动更新

规则来自 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)，每日北京时间凌晨 4:00 自动同步合并去重。

| 文件 | 来源 |
|:-----|:-----|
| `Direct_Rule.rule` | ChinaMax |
| `Proxy_Rule.rule` | Proxy + Global + GlobalMedia |
| `Reject_Rule.rule` | Advertising + Privacy |

可在 [Actions](https://github.com/pmjfff/Egern/actions) 手动触发更新。
