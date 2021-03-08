import scrapy
import logging


class PlayerStatsv2Spider(scrapy.Spider):
    name = 'player_statsV2'
    allowed_domains = ['sofifa.com']

    #handle_httpstatus_list = [302]
    #meta ={'dont_redirect': True}

    f = open("list_url_FINAL_souspartie3.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    
    def parse(self, response):
        
            name = response.xpath("/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div/h1/text()").get()
            poste_team = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/ul/li[2]/span/text()').get()
            date_maj = response.xpath('/html/body/header/div[2]/div/h2/div[2]/a/span[1]/text()').get()
            overall_rating = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[1]/div/span/text()').get()
            potential = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[2]/div/span/text()').get()
            prefered_foot = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[1]/text()').get()
            attacking_work_rate = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[5]/span/text()').get()
            defensive_work_rate = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[5]/span/text()').get()
            crossing = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[4]/div/ul/li[1]/span[1]/text()').get()
            finishing = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[4]/div/ul/li[2]/span[1]/text()').get()
            heading_accuracy = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[4]/div/ul/li[3]/span[1]/text()').get()
            short_passing = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[4]/div/ul/li[4]/span[1]/text()').get()
            volleys = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[4]/div/ul/li[5]/span[1]/text()').get()
            dribbling = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[5]/div/ul/li[1]/span[1]/text()').get()
            curve = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[5]/div/ul/li[2]/span[1]/text()').get()
            free_kick_accuracy = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[5]/div/ul/li[3]/span[1]/text()').get()
            long_passing = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[5]/div/ul/li[4]/span[1]/text()').get()
            ball_control = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[5]/div/ul/li[5]/span[1]/text()').get()
            acceleration = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[6]/div/ul/li[1]/span[1]/text()').get()
            sprint_speed = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[6]/div/ul/li[2]/span[1]/text()').get()
            agility = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[6]/div/ul/li[3]/span[1]/text()').get()
            reactions = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[6]/div/ul/li[4]/span[1]/text()').get()
            balance = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[6]/div/ul/li[5]/span[1]/text()').get()
            shot_power = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[7]/div/ul/li[1]/span[1]/text()').get()
            jumping = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[7]/div/ul/li[2]/span[1]/text()').get()
            stamina = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[7]/div/ul/li[3]/span[1]/text()').get()
            strength = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[7]/div/ul/li[4]/span[1]/text()').get()  
            long_shots = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[7]/div/ul/li[5]/span[1]/text()').get()
            aggression = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[8]/div/ul/li[1]/span[1]/text()').get()
            interceptions = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[8]/div/ul/li[2]/span[1]/text()').get()
            positioning = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[8]/div/ul/li[3]/span[1]/text()').get()
            vision = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[8]/div/ul/li[4]/span[1]/text()').get()
            penalties = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[8]/div/ul/li[5]/span[1]/text()').get()
            composure = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[8]/div/ul/li[6]/span/text()').get()
            marking = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[9]/div/ul/li[1]/span[1]/text()').get()
            standing_tackle = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[9]/div/ul/li[2]/span[1]/text()').get()
            sliding_tackle = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[9]/div/ul/li[3]/span[1]/text()').get()
            gk_diving = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[10]/div/ul/li[1]/span/text()').get()
            gk_handling = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[10]/div/ul/li[2]/span/text()').get()
            gk_kicking = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[10]/div/ul/li[3]/span/text()').get()
            gk_positioning = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[10]/div/ul/li[4]/span/text()').get()
            gk_reflexes = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[10]/div/ul/li[5]/span/text()').get()
            player_value = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[3]/div/text()').get()
            player_wage = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[4]/div/text()').get()
            player_release_clause = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[8]/span/text').get()
            url_scrapped = response.request.url
            club = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/h5/a/text()').get()
            weak_foot = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[2]/text()').get()
            international_reput = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[4]/text()').get()
            skill_move = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[3]/text()').get()
            age = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/text()').getall()

            yield {
                'date': date_maj,
                'player_name': name,
                'poste_team': poste_team,
                'overall_rating': overall_rating,
                'potential': potential,
                'prefered_foot': prefered_foot,
                'attacking_work_rate': attacking_work_rate[0:6],
                'defensive_work_rate': defensive_work_rate[8:],
                'crossing': crossing,
                'finishing': finishing,
                'heading_accuracy': heading_accuracy,
                'short_passing': short_passing,
                'volleys': volleys,
                'dribbling': dribbling,
                'curve': curve,
                'free_kick_accuracy': free_kick_accuracy,
                'long_passing': long_passing,
                'ball_control': ball_control,
                'acceleration': acceleration,
                'sprint_speed': sprint_speed,
                'agility': agility,
                'reactions': reactions,
                'balance': balance,
                'shot_power': shot_power,
                'jumping': jumping,
                'stamina': stamina,
                'strength': strength,
                'long_shots': long_shots,
                'aggression': aggression,
                'interceptions': interceptions,
                'positioning': positioning,
                'vision': vision,
                'penalties': penalties,
                'composure': composure,
                'marking': marking,
                'standing_tackle': standing_tackle,
                'sliding_tackle': sliding_tackle,
                'gk_diving': gk_diving,
                'gk_handling': gk_handling,
                'gk_kicking': gk_kicking,
                'gk_positioning': gk_positioning,
                'gk_reflexes': gk_reflexes,
                'player_value': player_value,
                'player_wage': player_wage,
                'player_release_clause':player_release_clause,
                'url_scrapped': url_scrapped,
                'club': club,
                'weak_foot': weak_foot,
                'international_reput': international_reput,
                'skill_move': skill_move,
                'age': age,

                 }
