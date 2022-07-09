import profit_parser.g2gprofitparser as g2g
import profit_parser.eldoprofitparser as eldo


g2g.start_parsing("g2ginput.csv", "g2goutput.csv",
    {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "cookie": ""  ### insert your cookie here
    })

eldo.start_parsing("eldoinput.csv", "eldooutput.csv",
    {
    "accept": "application/json, text/plain, */*",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "cookie": ""  ### insert your cookie here
    })