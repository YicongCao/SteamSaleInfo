## Steam 折扣信息推送

自动爬取 Steam 打折游戏，支持导出 csv、sqlite，支持按各维度查询折扣最佳的游戏，并推送到 Telegram、Slack、WxWork 等 Bot 平台。

- spider.py，爬虫模块
- csv2sqlite.py，读取csv、入库到sqlite
- query.py，按折扣力度、人气、好评率，查询游戏
- main.py，分别调用以上三个模块，发起 HTTP 请求，推送 Bot Message

![SteamBotDemo](image/steambotdemo.png)

示例推送：

```json
      
{
    "msgtype":"news",
    "news":{
        "articles":[
            {
                "title":"[最折扣] Just Cause 2",
                "description":"Just Cause 2,降价-92%,折后3元
Kane & Lynch 2: Dog Days,降价-92%,折后2元
The Official GamingTaylor Game, Great Job!,降价-92%,折后2元
",
                "url":"https://store.steampowered.com/app/8190/Just_Cause_2/?snr=1_7_7_204_150_1",
                "picurl":"https://media.st.dl.bscstorage.net/steam/apps/8190/capsule_sm_120.jpg?t=1543946597"
            },
            {
                "title":"[最人气] Eidos Anthology",
                "description":"Eidos Anthology,热度401340,折后305元
Euro Truck Simulator 2 Essentials,热度133723,折后68元
Euro Truck Simulator 2,热度125368,折后23元
",
                "url":"https://store.steampowered.com/bundle/4910/Eidos_Anthology/?snr=1_7_7_204_150_2",
                "picurl":"https://media.st.dl.bscstorage.net/steam/bundles/4910/gk3iu2bc8qnm5g46/capsule_sm_120.jpg?t=1511372795"
            },
            {
                "title":"[最人气] 爱上火车-Pure Station- Maitetsu:Pure Station",
                "description":"爱上火车-Pure Station- Maitetsu:Pure Station,好评率97%,折后52元
Euro Truck Simulator 2,好评率96%,折后23元
Euro Truck Simulator 2 Essentials,好评率96%,折后68元
",
                "url":"https://store.steampowered.com/app/880950/Pure_Station__MaitetsuPure_Station/?snr=1_7_7_204_150_3",
                "picurl":"https://media.st.dl.bscstorage.net/steam/apps/880950/capsule_sm_120.jpg?t=1539692294"
            }
        ]
    }
}
```