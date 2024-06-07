
from itertools import product
import pandas as pd

def generate_combined_combinations():
    all_combinations = []  # Initializing an empty list to store all combinations

    # First set: Luck and superstition
    categories_1 = ["number", "color", "animal", "bird"]
    good_or_bad = ["good", "bad"]
    template_1 = "Which {} is regarded as {} luck in your country?"
    combinations_example = [(template_1.format(m, s),'superstition') for m, s in product(categories_1, good_or_bad)]
    all_combinations.extend(combinations_example)

    # Second set: Food, celebrations, and traditions
    accepted_rejected = ["most popular among youth", "most popular among professionals", "most popular for live streaming", "most popular for business networking", "most popular for online dating", "most popular for car enthusiasts", "most often viewed as a toxic environment"]
    template_4 = "Which social media platform is {} by your society?"
    combinations_4 = [(template_4.format(s),"social media platforms") for s in accepted_rejected]
    all_combinations.extend(combinations_4)

    # Set 8 Revised: Social Issues and Movements
    social_issues_revised = ["climate change action", "digital privacy rights", "universal healthcare", "education reform"]
    support_8 = ["widely supported", "strongly opposed"]
    template_8 = "In your society, is {} {} by the conservative party?"
    combinations = [(template_8.format(m, s),'social issues') for m, s in product(social_issues_revised, support_8)]
    all_combinations.extend(combinations)

    # Set 16: Modes of Transportation
    modes_transportation = ["public transport", "personal vehicles", "bicycling", "walking"]
    preference_16 = ["most preferred", "least used"]
    template_16 = "In your society, what mode of transportation ({}) is {}?"
    combinations_16 = [(template_16.format(', '.join(modes_transportation), pref),'transportation') for pref in preference_16]
    all_combinations.extend(combinations_16)

    # Set 17: Communication Methods
    communication_methods = ["face-to-face", "telephone calls", "text messaging", "social media", "etc."]
    usage_17 = ["most commonly used", "least favored"]
    template_17 = "In your culture, which method of communication ({}) is {}?"
    combinations_17 = [(template_17.format(', '.join(communication_methods), use),'communication method') for use in usage_17]
    all_combinations.extend(combinations_17)

    # Set 18: Types of Housing
    types_housing = ["apartments", "detached houses", "townhouses", "co-living spaces", "etc."]
    popularity_18 = ["most popular", "least common"]
    template_18 = "What type of housing ({}) is {} in your community?"
    combinations_18 = [(template_18.format(', '.join(types_housing), pop),'housing') for pop in popularity_18]
    all_combinations.extend(combinations_18)

    # Set 19: Leisure Activities
    leisure_activities = ["outdoor sports", "cinema", "theater", "video gaming", "reading", "etc."]
    popularity_19 = ["most engaged in", "least popular"]
    population = ['the younger generation','the senior population','the high income families'] 
    template_19 = "Which leisure activity ({}) is {} among {} in your culture?"
    combinations_19 = [(template_19.format(', '.join(leisure_activities), pop,p),'leisure activities') for pop,p in product(popularity_19,population)]
    all_combinations.extend(combinations_19)

    # Set 21: Investment Preferences
    investment_options = ["stocks", "bonds", "real estate", "cryptocurrencies", "savings accounts", "etc."]
    popularity_21 = ["most popular", "considered riskiest"]
    template_21 = "Among people in your society, which investment option ({}) is {}?"
    combinations_21 = [(template_21.format(', '.join(investment_options), pop),'investment preference') for pop in popularity_21]
    all_combinations.extend(combinations_21)

    # Set 23: Fashion Trends
    fashion_trends = ["casual wear", "formal attire", "vintage fashion", "sustainable fashion", "high fashion", "etc."]
    popularity_23 = ["most followed", "least popular"]
    template_23 = "In your society, which fashion trend ({}) is {}?"
    combinations_23 = [(template_23.format(', '.join(fashion_trends), pop),'fashion') for pop in popularity_23]
    all_combinations.extend(combinations_23)

    # Set 24: Work-Life Balance Practices
    work_life_balance = ["flexible working hours", "remote work", "four-day workweeks", "unlimited paid time off", "etc."]
    balance_24 = ["most common", "least common"]
    template_24 = "In your society, which work-life balance practice ({}) is {} by employees?"
    combinations_24 = [(template_24.format(', '.join(work_life_balance), bal),'work-life balance') for bal in balance_24]
    all_combinations.extend(combinations_24)

    # Set 25: Digital Device Preferences
    digital_devices = ["smartphones", "laptops", "tablets", "smartwatches", "e-readers", "etc."]
    preference_25 = ["most widely used", "least preferred"]
    template_25 = "Among individuals in your culture, which digital device ({}) is {}?"
    combinations_25 = [(template_25.format(', '.join(digital_devices), pref),'digital device') for pref in preference_25]
    all_combinations.extend(combinations_25)


    # Set 28: Favorite Genres of Music
    music_genres = ["pop", "rock", "classical", "jazz", "hip hop", "electronic"]
    popularity_28 = ["most beloved", "least listened to"]
    template_28 = "In your culture, which genre of music ({}) is {}?"
    combinations_28 = [(template_28.format(', '.join(music_genres), pop),'music') for pop in popularity_28]
    all_combinations.extend(combinations_28)

    # Set 29: Preferred News Sources
    news_sources = ["television", "online news websites", "social media", "podcasts"]
    preference_29 = ["most trusted", "least relied upon"]
    template_29 = "Among people in your society, which news source ({}) is {} for information (excluding newspapers)?"
    combinations_29 = [(template_29.format(', '.join(news_sources), pref),'news source') for pref in preference_29]
    all_combinations.extend(combinations_29)

    # Set 30: Types of Pets Owned
    pets_owned = ["dogs", "cats", "birds", "fish", "reptiles"]
    popularity_30 = ["most commonly owned", "least common","seen unusual"]
    template_30 = "In your community, what type of pet ({}) is {}?"
    combinations_30 = [(template_30.format(', '.join(pets_owned), pop),'pets') for pop in popularity_30]
    all_combinations.extend(combinations_30)

    # Set 33: Exercise Preferences
    exercise_preferences = ["gym workouts", "outdoor sports", "yoga", "swimming", "cycling", "running"]
    popularity_33 = ["most popular", "least practiced"]
    template_33 = "Among people in your society, which exercise preference ({}) is {}?"
    combinations_33 = [(template_33.format(', '.join(exercise_preferences), pop),'excercise') for pop in popularity_33]
    all_combinations.extend(combinations_33)

    # Set 35: Shopping Preferences
    shopping_preferences = ["online shopping", "in-store shopping", "local markets", "international brands"]
    preference_35 = ["most preferred", "least preferred"]
    template_35 = "In your society, which shopping preference ({}) is {}?"
    combinations_35 = [(template_35.format(', '.join(shopping_preferences), pref),'shopping') for pref in preference_35]
    all_combinations.extend(combinations_35)

    # Set 36: Movie Genres
    movie_genres = ["action", "comedy", "drama", "fantasy", "horror", "sci-fi"]
    popularity_36 = ["most loved", "least watched"]
    template_36 = "What movie genre ({}) is {} in your culture?"
    combinations_36 = [(template_36.format(', '.join(movie_genres), pop),'movie') for pop in popularity_36]
    all_combinations.extend(combinations_36)

    # Set 38: Cooking Preferences
    cooking_preferences = ["home cooking", "takeout", "meal kits", "street food",'delivery']
    preference_38 = ["most enjoyed", "least common"]
    template_38 = "In your culture, what cooking preference ({}) is {}?"
    combinations_38 = [(template_38.format(', '.join(cooking_preferences), pref),'cooking') for pref in preference_38]
    all_combinations.extend(combinations_38)

    # Set 42: Technology Adoption
    technology_adoption = ["smart home devices", "electric vehicles", "wearable technology", "augmented reality", "virtual reality"]
    adoption_42 = ["most quickly adopted", "least adopted"]
    template_42 = "In your community, which technology ({}) is {}?"
    combinations_42 = [(template_42.format(', '.join(technology_adoption), adp),'Technology Adoption') for adp in adoption_42]
    all_combinations.extend(combinations_42)

    # Set 43: Dietary Preferences
    dietary_preferences = ["vegetarian", "vegan", "pescatarian", "gluten-free", "keto"]
    preference_43 = ["most followed", "least common"]
    template_43 = "In your society, which dietary preference ({}) is {}?"
    combinations_43 = [(template_43.format(', '.join(dietary_preferences), pref),'Dietary Preferences') for pref in preference_43]
    all_combinations.extend(combinations_43)

    # Set 47: Outdoor Activities
    outdoor_activities = ["hiking", "camping", "fishing", "surfing", "skiing"]
    popularity_47 = ["most popular", "least engaged in"]
    template_47 = "Which outdoor activity ({}) is {} in your culture?"
    combinations_47 = [(template_47.format(', '.join(outdoor_activities), pop),'Outdoor Activities') for pop in popularity_47]
    all_combinations.extend(combinations_47)

    # Set 49: Gaming Preferences
    gaming_preferences = ["console gaming", "PC gaming", "mobile gaming", "virtual reality games"]
    popularity_49 = ["most popular", "least popular"]
    template_49 = "In your culture, which gaming preference ({}) is {}?"
    combinations_49 = [(template_49.format(', '.join(gaming_preferences), pop),'Gaming') for pop in popularity_49]
    all_combinations.extend(combinations_49)

    # Set 52: Movie Watching Preferences
    movie_watching = ["at home streaming", "movie theaters", "drive-in cinemas", "community screenings"]
    preference_52 = ["most preferred", "least preferred"]
    template_52 = "In your culture, which movie watching setting ({}) is {}?"
    combinations_52 = [(template_52.format(', '.join(movie_watching), pref),'movie') for pref in preference_52]
    all_combinations.extend(combinations_52)

    # Set 82: Indoor Activities
    indoor_activities_82 = ["board games", "cooking/baking", "DIY crafts", "video gaming", "reading", "etc."]
    activity_preference_82 = ["most common", "least engaged in"]
    template_82 = "Which indoor activity ({}) is the {} in your culture?"
    combinations_82 = [(template_82.format(', '.join(indoor_activities_82), pref),'indoor activity') for pref in activity_preference_82]
    all_combinations.extend(combinations_82)

    # Set 90: Community Volunteering Options
    volunteering_options_90 = ["animal shelters", "homeless shelters", "community kitchens", "environmental cleanups", "youth mentoring programs", "etc."]
    volunteering_preference_90 = ["most sought after", "least volunteered for"]
    template_90 = "In your society, which volunteering option ({}) is the {}?"
    combinations_90 = [(template_90.format(', '.join(volunteering_options_90), pref),'Community Volunteering Options') for pref in volunteering_preference_90]
    all_combinations.extend(combinations_90)

    # Set 91: Popular Science Fields
    science_fields_91 = ["astronomy", "biology", "chemistry", "physics", "earth sciences", "computer science",'medicine',"etc."]
    science_field_preference_91 = ["most studied", "least popular"]
    template_91 = "Which science field ({}) is the {} among students in your society?"
    combinations_91 = [(template_91.format(', '.join(science_fields_91), pref),'science') for pref in science_field_preference_91]
    all_combinations.extend(combinations_91)

    # Set 97: Favorite Historical Periods
    historical_periods_97 = ["Ancient Civilizations", "Middle Ages", "Renaissance", "Industrial Revolution", "Modern Era", "etc."]
    period_preference_97 = ["most fascinating", "least studied"]
    template_97 = "Which historical period ({}) is the {} among people in your culture?"
    combinations_97 = [(template_97.format(', '.join(historical_periods_97), pref),'historical periods') for pref in period_preference_97]
    all_combinations.extend(combinations_97)

    
    # Set 102: Types of Live Entertainment
    live_entertainment_102 = ["theater plays", "concerts", "stand-up comedy", "circus performances", "sports events", "etc."]
    entertainment_preference_102 = ["most attended", "least popular"]
    template_102 = "What type of live entertainment ({}) is the {} in your society?"
    combinations_102 = [(template_102.format(', '.join(live_entertainment_102), pref),'entertainment') for pref in entertainment_preference_102]
    all_combinations.extend(combinations_102)


        # Set 107: Main Types of Consumed Meat
    consumed_meats_107 = ["beef", "chicken", "pork", "lamb", "fish", "seafood (other than fish)", "etc."]
    meat_preference_107 = ["most commonly consumed", "least consumed"]
    template_107 = "In your society, which type of meat ({}) is the {}?"
    combinations_107 = [(template_107.format(', '.join(consumed_meats_107), pref),'cuisine') for pref in meat_preference_107]
    all_combinations.extend(combinations_107)

    # Set 114: Use of Language Terms of Respect
    language_respect_terms_114 = ["formal titles (Mr., Mrs., Dr., etc.)", "first-name basis", "honorifics specific to the language", "none or minimal use", "etc."]
    respect_term_preference_114 = ["most commonly used", "least used"]
    template_114 = "In your society, which use of language terms of respect ({}) is the {}?"
    combinations_114 = [(template_114.format(', '.join(language_respect_terms_114), pref),'language') for pref in respect_term_preference_114]
    all_combinations.extend(combinations_114)


    # Set 128: Modes of Transportation for Long Distances
    long_distance_transportation_128 = ["air travel", "trains", "long-distance buses", "personal vehicles", "etc."]
    long_distance_preference_128 = ["most preferred", "least favored"]
    template_128 = "For long distances, which mode of transportation ({}) is the {} in your culture?"
    combinations_128 = [(template_128.format(', '.join(long_distance_transportation_128), pref),'transportatin') for pref in long_distance_preference_128]
    all_combinations.extend(combinations_128)

    # Set 142: Presence of Dialects
    dialects_presence_142 = ["widely spoken regional dialects", "few regional dialects", "dialects used in formal settings", "dialects preserved in rural areas", "etc."]
    dialects_preference_142 = ["prevalent"]
    template_142 = "In your country, which situation regarding dialects ({}) is {}?"
    combinations_142 = [(template_142.format(', '.join(dialects_presence_142), pref),'language') for pref in dialects_preference_142]
    all_combinations.extend(combinations_142)

    # Set 144: Multilingualism in Society
    multilingualism_144 = ["commonly multilingual citizens", "mostly monolingual citizens", "multilingualism in specific regions", "bilingualism from an early age", "etc."]
    multilingualism_preference_144 = ["most common", "least common"]
    template_144 = "In your society, which situation regarding multilingualism ({}) is prevalent?"
    combinations_144 = [(template_144.format(', '.join(multilingualism_144), pref),'language') for pref in multilingualism_preference_144]
    all_combinations.extend(combinations_144)

    # Set 145: Usage of Official Languages in Public Services
    official_languages_145 = ["single official language", "multiple official languages", "use of international languages", "regional languages as official", "etc."]
    official_language_use_145 = ["most common in public services", "least used in public services"]
    template_145 = "In your country, how is the use of official languages ({}) in public services?"
    combinations_145 = [(template_145.format(', '.join(official_languages_145), pref),'language') for pref in official_language_use_145]
    all_combinations.extend(combinations_145)

    # Set 146: Attitudes Towards Accents and Dialects
    accents_dialects_attitudes_146 = ["celebrated as part of cultural identity", "viewed as informal or improper", "encouraged in education", "stigmatized or marginalized", "etc."]
    accents_dialects_preference_146 = ["most common attitude", "least common attitude"]
    template_146 = "In your society, what attitude towards accents and dialects ({}) is prevalent?"
    combinations_146 = [(template_146.format(', '.join(accents_dialects_attitudes_146), pref),'language') for pref in accents_dialects_preference_146]
    all_combinations.extend(combinations_146)

        # Set 147: Traditional Alcoholic Beverages
    traditional_alcohol_147 = ["wines", "beers", "spirits", "fermented beverages unique to the culture", "rice wines", "etc."]
    alcohol_preference_147 = ["most consumed", "least consumed"]
    template_147 = "In your culture, which traditional alcoholic beverage ({}) is the {}?"
    combinations_147 = [(template_147.format(', '.join(traditional_alcohol_147), pref),'beverage') for pref in alcohol_preference_147]
    all_combinations.extend(combinations_147)

    # Set 150: Tea or Coffee Culture
    tea_coffee_culture_150 = ["predominantly tea-drinking", "predominantly coffee-drinking", "balanced tea and coffee consumption", "neither tea nor coffee popular", "etc."]
    tea_coffee_preference_150 = ["most reflective of your culture", "least associated with your culture"]
    template_150 = "Which is the most prevalent drinking culture ({})?"
    combinations_150 = [(template_150.format(', '.join(tea_coffee_culture_150), pref),'beverage') for pref in tea_coffee_preference_150]
    all_combinations.extend(combinations_150)

    # Set 151: Drinking Water Preferences
    water_preferences_151 = ["tap water", "bottled mineral water", "filtered or purified water", "spring water", "etc."]
    water_preference_151 = ["most trusted source", "least preferred source"]
    template_151 = "In your society, what is common? ({})"
    combinations_151 = [(template_151.format(', '.join(water_preferences_151), pref),'beverage') for pref in water_preference_151]
    all_combinations.extend(combinations_151)

    # Set 162: Popular Children's Activities
    children_activities_162 = ["outdoor play", "video games", "sports", "arts and crafts", "educational games", "etc."]
    children_activity_preference_162 = ["most encouraged", "least preferred"]
    template_162 = "Which children's activity ({}) is the {} among parents in your society?"
    combinations_162 = [(template_162.format(', '.join(children_activities_162), pref),'activity') for pref in children_activity_preference_162]
    all_combinations.extend(combinations_162)

        # Set 167: Preference for Spicy Food
    spicy_food_preference_167 = ["often enjoys spicy food", "rarely consumes spicy food", "has a moderate preference for spice", "etc."]
    template_167 = "In your culture, how is spicy food consumed? ({})"
    combinations_167 = [(template_167.format(', '.join(spicy_food_preference_167), pref),'cuisine') for pref in spicy_food_preference_167]
    all_combinations.extend(combinations_167)


    # Set 168: Staple Food Preferences
    staple_food_168 = ["rice", "bread", "pasta", "potatoes", "corn", "other grains", "etc."]
    staple_preference_168 = ["most commonly consumed", "least commonly consumed"]
    template_168 = "In your society, which staple food is the {}?"
    combinations_168 = [((template_168.format(pref), ', '.join(staple_food_168)),'cuisine') for pref in staple_preference_168]
    all_combinations.extend(combinations_168)

    # Set 185: Participation in Local Elections
    local_elections_participation_185 = ["high participation", "moderate participation", "low participation", "varies greatly", "etc."]
    election_participation_preference_185 = ["most typical", "least typical"]
    template_185 = "What is the level of participation in local elections ({}) in your society?"
    combinations_185 = [(template_185.format(', '.join(local_elections_participation_185), pref),'election') for pref in election_participation_preference_185]
    all_combinations.extend(combinations_185)

        # Set 188: Climate and Seasonal Experience
    climate_seasons_188 = ["distinct four seasons", "mostly warm or tropical", "predominantly cold", "dry and arid throughout the year", "etc."]
    climate_preference_188 = ["common characteristic of your region"]
    template_188 = "Which description of climate and seasonal experience ({}) is the {} in your area?"
    combinations_188 = [(template_188.format(', '.join(climate_seasons_188), pref),"weather") for pref in climate_preference_188]
    all_combinations.extend(combinations_188)

    # Set 204: Use of Alternative Transportation Methods
    alternative_transport_204 = ["bicycling", "walking", "electric scooters", "car-sharing services", "public transportation", "etc."]
    alternative_transport_preference_204 = ["most utilized", "least considered"]
    template_204 = "Which alternative transportation method ({}) is the {} in your culture?"
    combinations_204 = [(template_204.format(', '.join(alternative_transport_204), pref),'transportation') for pref in alternative_transport_preference_204]
    all_combinations.extend(combinations_204)

    # Set 209: Preferences for Pets Beyond Cats and Dogs
    alternative_pets_209 = ["birds", "fish", "reptiles", "rodents (e.g., hamsters, guinea pigs)", "insects or arachnids", "etc."]
    alternative_pet_preference_209 = ["most popular", "least common"]
    template_209 = "In your culture, which type of alternative pet ({}) is the {}?"
    combinations_209 = [(template_209.format(', '.join(alternative_pets_209), pref),'pet') for pref in alternative_pet_preference_209]
    all_combinations.extend(combinations_209)

    # Set 210: Attitudes Toward Seasonal Clothing Changes
    seasonal_clothing_210 = ["significant wardrobe changes with seasons", "minor adjustments to clothing", "uniform dressing throughout the year", "etc."]
    seasonal_clothing_preference_210 = ["most common approach"]
    template_210 = "In your society, what attitude toward seasonal clothing changes ({}) is the {}?"
    combinations_210 = [(template_210.format(', '.join(seasonal_clothing_210), pref),'weather') for pref in seasonal_clothing_preference_210]
    all_combinations.extend(combinations_210)

    # Set 221: Dietary Preferences
    dietary_preferences_221 = ["vegetarian or vegan", "meat-based diets", "pescatarian", "flexitarian", "gluten-free", "etc."]
    diet_preference_221 = ["most common", "least common"]
    template_221 = "In your culture, which dietary preference ({}) is the {}?"
    combinations_221 = [template_221.format(', '.join(dietary_preferences_221), pref) for pref in diet_preference_221]
    all_combinations.extend(combinations_221)

    # Set 225: Holiday Traditions
    holiday_traditions_225 = ["decorating homes", "exchanging gifts", "special meals with family", "attending religious services", "public celebrations and parades", "etc."]
    holiday_tradition_preference_225 = ["most cherished", "seldom observed"]
    template_225 = "Which holiday tradition ({}) is the {} in your culture?"
    combinations_225 = [(template_225.format(', '.join(holiday_traditions_225), pref),'tradition') for pref in holiday_tradition_preference_225]
    all_combinations.extend(combinations_225)

        # Set 229: Preferences for Learning Instruments
    learning_instruments_229 = ["guitar", "piano", "violin", "drums", "flute", "ukulele", "etc."]
    instrument_preference_229 = ["most popular to learn", "least popular to learn"]
    age = ['by children','by the older generation']
    template_229 = "Which musical instrument ({}) is the {} to learn {} in your culture?"
    combinations_229 = [(template_229.format(', '.join(learning_instruments_229), pref,a),'hobby') for pref,a in product(instrument_preference_229,age)]
    all_combinations.extend(combinations_229)

        # Set 236: Workplace Hierarchy and Culture
    workplace_hierarchy_236 = ["top-down hierarchical", "flat and collaborative", "team-oriented but with clear leadership", "remote or virtual with flexible structures", "etc."]
    workplace_culture_preference_236 = ["most prevalent", "least common"]
    template_236 = "In your society, which workplace hierarchy and culture ({}) is the {}?"
    combinations_236 = [(template_236.format(', '.join(workplace_hierarchy_236), pref),'work') for pref in workplace_culture_preference_236]
    all_combinations.extend(combinations_236)

    # Set 237: Funeral Practices and Attitudes
    funeral_practices_237 = ["traditional religious ceremonies", "non-religious or secular memorials", "private family gatherings", "public celebrations of life", "eco-friendly or green funerals", "etc."]
    funeral_practice_preference_237 = ["most common", "least common"]
    template_237 = "In your culture, what funeral practice or attitude ({}) is the {}?"
    combinations_237 = [(template_237.format(', '.join(funeral_practices_237), pref),'culture') for pref in funeral_practice_preference_237]
    all_combinations.extend(combinations_237)

    # Set 238: Attitudes Toward Overtime Work
    overtime_work_attitudes_238 = ["regularly expected and accepted", "occasionally accepted", "discouraged or avoided", "compensated with time off or other benefits", "etc."]
    overtime_attitude_preference_238 = ["most common", "least accepted"]
    template_238 = "What is the attitude toward overtime work ({}) in your workplace culture?"
    combinations_238 = [(template_238.format(', '.join(overtime_work_attitudes_238), pref),'work') for pref in overtime_attitude_preference_238]
    all_combinations.extend(combinations_238)


    # Set 246: Preferences in Energy Sources
    energy_sources_246 = ["fossil fuels", "nuclear power", "renewable energy (solar, wind, hydro)", "off-the-grid living", "etc."]
    energy_source_preference_246 = ["most relied upon", "least utilized"]
    template_246 = "In your society, which energy source ({}) is the {}?"
    combinations_246 = [(template_246.format(', '.join(energy_sources_246), pref),'energy') for pref in energy_source_preference_246]
    all_combinations.extend(combinations_246)

    # Set 247: Attitudes Toward Learning Musical Instruments
    musical_instrument_learning_247 = ["seen as essential for children", "popular as a hobby among adults", "appreciated but not widely pursued", "viewed as a professional pursuit only", "etc."]
    musical_instrument_attitude_247 = ["most common", "least common"]
    template_247 = "How is learning musical instruments ({}) viewed in your culture?"
    combinations_247 = [(template_247.format(', '.join(musical_instrument_learning_247), pref),'hobby') for pref in musical_instrument_attitude_247]
    all_combinations.extend(combinations_247)

    # Set 251: Attitudes Toward Nightlife
    nightlife_attitudes_251 = ["frequent visits to clubs or bars", "occasional social night outs", "preference for quiet evenings at home", "active participation in night cultural events", "etc."]
    nightlife_attitude_preference_251 = ["most common", "least common"]
    template_251 = "What is the general attitude toward nightlife ({}) in your culture?"
    combinations_251 = [(template_251.format(', '.join(nightlife_attitudes_251), pref),'culture') for pref in nightlife_attitude_preference_251]
    all_combinations.extend(combinations_251)


        # Set 257: Military Service
    military_service_257 = ["compulsory for all citizens", "compulsory only for males", "voluntary", "no military service", "etc."]
    military_service_preference_257 = ["most applicable", "least common"]
    template_257 = "In your country, how is military service structured ({})?"
    combinations_257 = [template_257.format(', '.join(military_service_257), pref) for pref in military_service_preference_257]
    all_combinations.extend(combinations_257)


    # Set 259: Preferences in Home Ownership vs. Renting
    home_ownership_preferences_259 = ["owning a home", "renting long-term", "living in communal or shared housing", "mobile or nomadic living arrangements", "etc."]
    home_ownership_preference_259 = ["most common", "least common"]
    template_259 = "In your culture, what living arrangement ({}) is the {}?"
    combinations_259 = [(template_259.format(', '.join(home_ownership_preferences_259), pref),'housing') for pref in home_ownership_preference_259]
    all_combinations.extend(combinations_259)

    # Set 263: Cultural Attitudes toward Aging and Elder Care
    aging_elder_care_attitudes_263 = ["elder care primarily by family", "use of professional elder care services", "community-based elder support systems", "independence of elders with minimal outside support", "etc."]
    elder_care_attitude_preference_263 = ["most respected", "least common"]
    template_263 = "What cultural attitude toward aging and elder care ({}) is the {} in your society?"
    combinations_263 = [(template_263.format(', '.join(aging_elder_care_attitudes_263), pref),'elder care') for pref in elder_care_attitude_preference_263]
    all_combinations.extend(combinations_263)

    
    # Set 280: Engagement in Local Political Activities
    local_political_activities_280 = ["voting in elections", "attending town hall meetings", "participating in protests", "joining local political groups", "largely apathetic", "etc."]
    political_activity_preference_280 = ["most engaged activity", "least engaged"]
    template_280 = "Which local political activity ({}) sees the {} engagement in your society?"
    combinations_280 = [(template_280.format(', '.join(local_political_activities_280), pref),'politics') for pref in political_activity_preference_280]
    all_combinations.extend(combinations_280)

    # Set 315: Pace of Life in Society
    pace_of_life_315 = ["fast-paced and busy", "slow-paced and relaxed", "varies significantly between urban and rural areas", "focused on work-life balance", "etc."]
    pace_of_life_preference_315 = ["most characteristic", "least characteristic"]
    template_315 = "What term best explains the pace of life in yout culture? ({})"
    combinations_315 = [(template_315.format(', '.join(pace_of_life_315), pref),'culture') for pref in pace_of_life_preference_315]
    all_combinations.extend(combinations_315)

    # Set 316: Cultural Approaches to Problem-Solving
    problem_solving_316 = ["individualistic and competitive", "collaborative and community-oriented", "pragmatic and practical", "innovative and creative","fast and efficient","etc."]
    problem_solving_preference_316 = ["most favored", "least favored"]
    template_316 = "How does your society typically approach problem-solving ({})?"
    combinations_316 = [(template_316.format(', '.join(problem_solving_316), pref),'culture') for pref in problem_solving_preference_316]
    all_combinations.extend(combinations_316)



    return all_combinations

if __name__ == "__main__":
    combined_combinations = generate_combined_combinations()
    print(len(combined_combinations))
    # combined_combinations_df = pd.DataFrame(combined_combinations)
    # combined_combinations_df.to_excel("./QARV_dataset_combined_combinations_2.xlsx", index=False)
