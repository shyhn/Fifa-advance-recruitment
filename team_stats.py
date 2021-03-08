import scrapy


class TeamStatsSpider(scrapy.Spider):
    name = 'team_stats'
    allowed_domains = ['sofifa.com']
    
    #handle_httpstatus_list = [302]
    #meta ={'dont_redirect': True}

    f = open("list_url_team_part1_part2.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    
    def parse(self, response):
        
            date_maj = response.xpath('/html/body/header/div[2]/div/h2/div[2]/a/span[1]/text()').get()
            url_scrapped = response.request.url
            name = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/h1/text()').get()
            buildUpPlaySpeed = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[1]/span[2]/span/text()').get()
            buildUpPlaySpeedClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[1]/span[2]/text()').get()
            buildUpPlayDribbling =  response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[2]/span/span/text()').get()
            buildUpPlayDribblingClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[2]/span/text()').get()
            buildUpPlayPassing = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[3]/span[2]/span/text()').get()
            buildUpPlayPassingClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[3]/span[2]/text()').get()
            buildUpPlayPositioningClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[4]/span[2]/text()').get()
            chanceCreationPassing = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[5]/span[2]/span/text()').get()
            chanceCreationPassingClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[5]/span[2]/text()').get()
            chanceCreationCrossing = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[6]/span[2]/span/text()').get()
            chanceCreationCrossingClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[6]/span[2]/text()').get()
            chanceCreationShooting = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[7]/span[2]/span/text()').get()
            chanceCreationShootingClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[7]/span[2]/text()').get()
            chanceCreationPositioningClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[8]/span[2]/text()').get()
            defencePressure = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[9]/span[2]/span/text()').get()
            defencePressureClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[9]/span[2]/text()').get()
            defenceAggression = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[10]/span[2]/span/text()').get()
            defenceAggressionClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[10]/span[2]/text()').get()
            defenceTeamWidth = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[11]/span[2]/span/text()').get()
            defenceTeamWidthClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[11]/span[2]/span/text()').get()
            defenceDefenderLineClass = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/dl/dd[12]/span[2]/text()').get()
            stadium = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[1]/text()').get()
            rival_team = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[2]/a/text()').get()
            international_prestige = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[3]/span/text()').get()
            domestic_prestige = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[4]/span/text()').get()
            transfer_budget = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[5]/text()').getall()
            start_xi_age_avg = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[6]/text()').get()
            all_team_age_avg = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[7]/text()').get()
            captain = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[8]/a/text()').get()
            short_free_kick = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[9]/a/text()').get()
            long_free_kick = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[10]/a/text()').get()
            left_short_free_kick = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[11]/a/text()').get()
            right_short_free_kick = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[12]/a/text()').get()
            penalties = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[13]/a/text()').get()
            left_corner = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[14]/a/text()').get()
            right_corner = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/ul/li[15]/a/text()').get()
            ligue = response.xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/a[2]/text()').get()

            yield {
                'date': date_maj,
                'url_scrapped': url_scrapped,
                'name': name,
                'buildUpPlaySpeed' : buildUpPlaySpeed,
                'buildUpPlaySpeedClass' : buildUpPlaySpeedClass,
                'buildUpPlayDribbling' : buildUpPlayDribbling,
                'buildUpPlayDribblingClass' : buildUpPlayDribblingClass,
                'buildUpPlayPassing' : buildUpPlayPassing,
                'buildUpPlayPassingClass': buildUpPlayPassingClass,
                'buildUpPlayPositioningClass': buildUpPlayPositioningClass,
                'chanceCreationPassing': chanceCreationPassing,
                'chanceCreationPassingClass': chanceCreationPassingClass,
                'chanceCreationCrossing': chanceCreationCrossing,
                'chanceCreationCrossingClass': chanceCreationCrossingClass,
                'chanceCreationShooting': chanceCreationShooting,
                'chanceCreationShootingClass': chanceCreationShootingClass,
                'chanceCreationPositioningClass': chanceCreationPositioningClass,
                'defencePressure': defencePressure,
                'defencePressureClass': defencePressureClass,
                'defenceAggression': defenceAggression,
                'defenceAggressionClass': defenceAggressionClass,
                'defenceTeamWidth': defenceTeamWidth,
                'defenceTeamWidthClass': defenceTeamWidthClass,
                'defenceDefenderLineClass': defenceDefenderLineClass,
                'stadium': stadium,
                'rival_team' : rival_team,
                'international_prestige' : international_prestige,
                'domestic_prestige': domestic_prestige,
                'transfer_budget' : transfer_budget,
                'start_xi_age_avg': start_xi_age_avg,
                'all_team_age_avg': all_team_age_avg,
                'captain': captain,
                'short_free_kick': short_free_kick,
                'long_free_kick': long_free_kick,
                'left_short_free_kick': left_short_free_kick,
                'right_short_free_kick': right_short_free_kick,
                'penalties': penalties,
                'left_corner': left_corner,
                'right_corner': right_corner,
                'ligue': ligue

                 }
