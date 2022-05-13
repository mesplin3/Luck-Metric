import math
from classes import *

def get_text(file_name):  # reads the file
    with open(file_name) as test_file:
        read_data = test_file.read()
        return read_data


def text_format(text):  # converts a file into a 2d list by line and by word
    text_by_word = [[]]
    text_by_line = text.splitlines()
    for i in range(len(text_by_line)):
        line_by_word = text_by_line[i].split()
        text_by_word.append(line_by_word)
    return text_by_word


def is_word_in_line(word, line):  # checks to see if a word is in a list of words
    b = False
    for i in range(len(line)):
        if word in line:
            b = True
    return b


def get_word_in_line_index_num(word, line):  # find location of a word in the list, return -1 if not found
    index_num = -1
    for i in range(len(line)):
        if word == line[i]:
            index_num = i
    return index_num


def swap_words_in_line(old_word, new_word, line):  # formats the line by replace every instance of word1 with word2 in list
    for i in range(len(line)):
        if line[i] == old_word:
            line[i] = new_word
    return line


def get_lower_case_string_list(old_line):  # makes a string list all lowercase
    new_line = []
    for i in range(len(old_line)):
        new_line.append(old_line[i].lower())
    return new_line


def format_name(name):  # format the move, so it is lowercase and remove '!'
    move_name_formatted = name.lower()
    move_name_formatted = move_name_formatted.replace('!', '')
    return move_name_formatted


def get_speed(pokemon_species, base_stats_text):  # finds speed of a Pokémon (Beedrill, Bulbasaur, etc.) returns -1 if can't find it
    for i in range(len(base_stats_text)):
        if is_word_in_line(pokemon_species, base_stats_text[i]):
            return int(base_stats_text[i][6])
    return -1


def is_high_crit(move_name, moves_info_text):  # determines if the move was a high_crit move
    b = False
    for i in range(len(moves_info_text)):
        if is_word_in_line(move_name, moves_info_text[i]):
            if is_word_in_line('high_crit', moves_info_text[i]):
                b = True
    return b


def get_crit_percent(pokemon_base_speed, high_crit_bool=False):  # returns a value for the chance of getting a crit
    if not high_crit_bool:
        return float(min((pokemon_base_speed * 100)/512, 100*255/256))
    else:
        return float(min((pokemon_base_speed * 100)/64, 100*255/256))


def is_crit(line):  # determines if the line is a crit
    b = False
    if is_word_in_line('Critical', line):
        b = True
    return b


def get_move_accuracy(move_name, ally_status, text):  # finds the accuracy of the move
    for i in range(len(text)):
        if move_name in text[i]:
            if ally_status:
                return text[i][1]
            else:
                return text[i][2]
    return -1


def get_accuracy_probability_from_accuracy_level(level):
    # https://bulbapedia.bulbagarden.net/wiki/Stat#Stage_multipliers
    if level == -6:
        return 25/100
    elif level == -5:
        return 28/100
    elif level == -4:
        return 33/100
    elif level == -3:
        return 40/100
    elif level == -2:
        return 50/100
    elif level == -1:
        return 66/100
    elif level == 0:
        return 100/100
    elif level == 1:
        return 150/100
    elif level == 2:
        return 200/100
    elif level == 3:
        return 250/100
    elif level == 4:
        return 300/100
    elif level == 5:
        return 350/100
    elif level == 6:
        return 400/100
    else:
        return -1


def get_accuracy_probability_from_evasion_level(level):
    # https://bulbapedia.bulbagarden.net/wiki/Stat#Stage_multipliers
    if level == 6:
        return 25/100
    elif level == 5:
        return 28/100
    elif level == 4:
        return 33/100
    elif level == 3:
        return 40/100
    elif level == 2:
        return 50/100
    elif level == 1:
        return 66/100
    elif level == 0:
        return 100/100
    elif level == -1:
        return 150/100
    elif level == -2:
        return 200/100
    elif level == -3:
        return 250/100
    elif level == -4:
        return 300/100
    elif level == -5:
        return 350/100
    elif level == -6:
        return 400/100
    else:
        return -1


def get_accuracy_stat_modifier(pokemon_accuracy_level, opposing_pokemon_evasion_level):
    # chance of a 100 accurate move hitting given the accuracy (de)buffs and evasion (de)buffs
    probability_from_accuracy_level = get_accuracy_probability_from_accuracy_level(pokemon_accuracy_level)
    probability_from_evasion_level = get_accuracy_probability_from_evasion_level(opposing_pokemon_evasion_level)
    return min(probability_from_accuracy_level * probability_from_evasion_level, 1)


def get_confusion_status():  # determines if the Pokémon is confused, INCOMPLETE
    return False


def get_paralysis_status():  # determines if the Pokémon is paralyzed, INCOMPLETE
    return False


def get_status_condition_accuracy_modifier():
    # determine probability a 100 accurate move hitting from status conditions, INCOMPLETE
    # https://bulbapedia.bulbagarden.net/wiki/Status_condition#Paralysis,
    p = 1
    paralysis_status = get_paralysis_status()
    if paralysis_status:
        p = p * (1 - 0.25)
    # https://bulbapedia.bulbagarden.net/wiki/Status_condition#Confusion
    confusion_status = get_confusion_status()
    if confusion_status:
        p = p * (1 - 0.5)
    return p


def is_move_hit(line):  # determines if a move hit by checking the after the attack for a miss
    b = True
    if is_word_in_line('missed!', line):
        b = False
    return b


def get_move_effect_chance(move_name, move_text):  # gets the chance of the effect from a move,
    # returns 0 if no effect,
    # returns -1 if move_name is unlisted
    for i in range(len(move_text)):
        if move_name in move_text[i]:
            if len(move_text[i]) == 5:
                return move_text[i][3]
            else:
                return 0
    return -1


def get_move_effect_keyword(move_name, move_text):  # gets the keyword of the effect from a move,
    # returns NA if no effect,
    # returns unlisted if move_name is unlisted
    for i in range(len(move_text)):
        if move_name in move_text[i]:
            if len(move_text[i]) == 5:
                return move_text[i][4]
            else:
                return 'NA'
    return 'unlisted'


def get_probability_accuracy_event(move_name, ally_status, move_text,
                                   pokemon_accuracy_level, opposing_pokemon_evasion_level,
                                   line_after_attack):
    move_accuracy = float(get_move_accuracy(move_name, ally_status, move_text))
    # get move accuracy; check
    accuracy_stat_modifier = float(get_accuracy_stat_modifier(pokemon_accuracy_level, opposing_pokemon_evasion_level))
    # get chance of 100 accuracy move to hit target; check
    status_condition_accuracy_modifier = float(get_status_condition_accuracy_modifier())
    # account for status conditions;
    move_hit = is_move_hit(line_after_attack)
    # determine if the move hit or not; check
    if move_hit:
        p = move_accuracy * accuracy_stat_modifier * status_condition_accuracy_modifier
    else:
        p = 1 - (move_accuracy * accuracy_stat_modifier * status_condition_accuracy_modifier)
    return p


def get_probability_critical_event(pokemon_species, pokemon_base_stats_text, move_name, moves_info_text, line_after_attack):
    # find the percentage that a move crits or doesn't crit
    pokemon_species = format_name(pokemon_species).capitalize()
    speed = get_speed(pokemon_species, pokemon_base_stats_text)  # get Pokémon's speed
    high_crit = is_high_crit(move_name, moves_info_text)  # get high_crit bool
    crit_percentage = get_crit_percent(speed, high_crit)  # get critical hit chance
    if is_crit(line_after_attack):
        return crit_percentage/100
    else:
        return (100 - crit_percentage)/100


def get_probability_effect_event(move_name, moves_info_text, line):  # move_name needs a '_' for spaces,
    # move info text is a document that has the probabilities for moves, and
    # line is a list of strings that look for a keyword related to the effect of the move
    move_effect_chance = get_move_effect_chance(move_name, moves_info_text)  # get move's effect chance; check
    move_effect_keyword = get_move_effect_keyword(move_name, moves_info_text)  # get the keyword of the effect

    if move_effect_keyword == 'NA' or move_effect_keyword == 'unlisted':
        # if effect is NA or an unlisted move, then return 1 for probability
        return -1
    elif move_effect_keyword in line:
        return float(move_effect_chance)
    elif move_effect_keyword not in line:
        return 1-float(move_effect_chance)
    else:
        # if there is an error, then return -1
        return -1


def is_move_in_line(line):
    return is_word_in_line('used', line)


def is_ally(line):
    return not is_word_in_line('Enemy', line)


def get_pokemon_name(line):  # determine the name of the Pokémon involved
    if is_move_in_line(line):
        i = get_word_in_line_index_num('used', line)
        return line[i - 1]


def get_move_used(line):  # determine the move name involved
    if is_move_in_line(line):
        i = get_word_in_line_index_num('used', line)

        if len(line) - get_word_in_line_index_num('used', line) > 2:
            return line[i+1] + '_' + line[i+2]
        else:
            return line[i + 1]


def get_event_index(text):  # determine which line an event is on
    event_index = []
    for i in range(len(text)):
        if is_move_in_line(text[i]):
            event_index.append(i)
    return event_index


def get_goodness_bool(ally, line_after_attack):
    if ally:
        if is_move_hit(line_after_attack):
            goodness_bool = True
        elif not is_move_hit(line_after_attack):
            goodness_bool = False
    else:
        if is_move_hit(line_after_attack):
            goodness_bool = False
        elif not is_move_hit(line_after_attack):
            goodness_bool = True
    return goodness_bool


def get_accuracy_event_list(event_text, event_index, move_text):  # define a list of events related to accuracy
    accuracy_event_list = []
    for i in range(len(event_index)):
        pokemon_species = get_pokemon_name(event_text[event_index[i]])
        ally = is_ally(event_text[event_index[i]])
        move_name = get_move_used(event_text[event_index[i]])
        move_name = format_name(move_name)
        goodness_bool = get_goodness_bool(ally, event_text[1 + event_index[i]])
        event = AccuracyEvent(event_index[i], ally, pokemon_species, 'accuracy_event', goodness_bool, 1)
        p = get_probability_accuracy_event(move_name, ally, move_text, 0, 0, event_text[1 + event_index[i]])
        event.probability = p
        accuracy_event_list.append(event)

    return accuracy_event_list


def is_critable_move(move_name, move_critable_text):
    for i in range(len(move_critable_text)):
        if move_name in move_critable_text[i]:
            if move_critable_text[i][1] == 'FALSE':
                return False
            elif move_critable_text[i][1] == 'TRUE':
                return True


def is_critable_event(event_text, index_num, move_critable_text):
    # get move name, verify if it is critable, check next line for a missed!, if it passes then it is a critable event
    move_used = get_move_used(event_text[index_num])
    move_used = format_name(move_used)
    if is_critable_move(move_used, move_critable_text):
        if is_move_hit(event_text[index_num + 1]):
            return True
        else:
            return False
    else:
        return False


def get_goodness_bool_crits(ally_bool, line):
    goodness_bool = True
    if ally_bool:
        if not is_crit(line):
            goodness_bool = False
    else:
        if is_crit(line):
            goodness_bool = False
    return goodness_bool


def get_critical_event_list(event_text, event_index, pokemon_base_stats_text, moves_info_text, move_critability_text):
    # define a list of critical hit related events
    # pokemon_species, pokemon_base_stats_text, move_name, moves_info_text, line_after_attack
    critical_event_list = []
    critical_event_index = []
    for j in range(len(event_index)):
        if is_critable_event(event_text, event_index[j], move_critability_text):
            critical_event_index.append(j)

    for i in range(len(critical_event_index)):
        pokemon_species = get_pokemon_name(event_text[event_index[critical_event_index[i]]])
        pokemon_species = format_name(pokemon_species)
        move_name = get_move_used(event_text[event_index[critical_event_index[i]]])
        move_name = format_name(move_name)
        ally = is_ally(event_text[event_index[critical_event_index[i]]])
        goodness_bool = get_goodness_bool_crits(ally, event_text[1 + event_index[critical_event_index[i]]])
        event = CriticalEvent(event_index[critical_event_index[i]], ally, pokemon_species, 'critical_event', goodness_bool, 1)
        p = get_probability_critical_event(pokemon_species,
                                           pokemon_base_stats_text,
                                           move_name,
                                           moves_info_text,
                                           event_text[event_index[critical_event_index[i]]+1])
        event.probability = p
        critical_event_list.append(event)
    return critical_event_list


def is_effect_move(move_name, move_text):
    for i in range(len(move_text)):
        if move_name in move_text[i]:
            if len(move_text[i]) >= 5:
                return True
            else:
                return False


def get_effect_event_list(event_text, event_index, moves_info_text):
    # get_probability_effect_event(move_name, moves_info_text, line)
    effect_event_list = []
    effect_event_index = []
    for j in range(len(event_index)):
        move_name = get_move_used(event_text[event_index[j]])
        move_name = format_name(move_name)
        if is_effect_move(move_name, moves_info_text):
            effect_event_index.append(j)

    for i in range(len(effect_event_index)):
        pokemon_species = get_pokemon_name(event_text[event_index[effect_event_index[i]]])
        pokemon_species = format_name(pokemon_species)
        ally = is_ally(event_text[event_index[effect_event_index[i]]])
        goodness_bool = get_goodness_bool(ally, event_text[1 + event_index[i]])
        event = EffectEvent(event_index[effect_event_index[i]], ally, pokemon_species, 'effect_event', goodness_bool, 1)
        p = get_probability_effect_event(move_name, moves_info_text, event_text[event_index[effect_event_index[i]]+1])
        event.probability = p
        effect_event_list.append(event)

    return effect_event_list


def get_event_list(accuracy_event_list, critical_event_list):
    event_list = []
    for i in range(len(accuracy_event_list)):
        event_list.append(accuracy_event_list[i])
    for i in range(len(critical_event_list)):
        event_list.append(critical_event_list[i])
    # for i in range(len(effect_event_list)):
    #     event_list.append(effect_event_list[i])
    return event_list


def get_ally_event_list(event_list):  # define a subset of the list of events to account for events that only involve ally Pokémon
    ally_event_list = []
    for i in range(len(event_list)):
        if event_list[i].ally_bool:
            ally_event_list.append(event_list[i])
    return ally_event_list


def get_enemy_event_list(event_list):  # define a subset of the list of events to account for events that only involve enemy Pokémon
    enemy_event_list = []
    for i in range(len(event_list)):
        if not event_list[i].ally_bool:
            enemy_event_list.append(event_list[i])
    return enemy_event_list


def get_good_event_list(event_list):  # define a subset of the list of events for only good events
    good_event_list = []
    for i in range(len(event_list)):
        if event_list[i].goodness_bool:
            good_event_list.append(event_list[i])
    return good_event_list


def get_bad_event_list(event_list):  # define a subset of the list of events for only good events
    bad_event_list = []
    for i in range(len(event_list)):
        if not event_list[i].goodness_bool:
            bad_event_list.append(event_list[i])
    return bad_event_list


def get_surpise(event_list):
    surprise = 0
    for i in range(len(event_list)):
        if event_list[i].probability > 0:
            surprise = surprise - math.log2(float(event_list[i].probability))
    return surprise
