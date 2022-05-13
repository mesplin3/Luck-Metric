from functions import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
base_stats = get_text('pokemon base stats.txt')
base_stats_formatted = text_format(base_stats)

move_info = get_text('gen1 moves.txt')
move_info_formatted = text_format(move_info)

# filenames_text = get_text('filenames.txt')
# filenames_text_formatted = text_format(filenames_text)
# for j in range(-1 + len(filenames_text_formatted)):

filenames_text_formatted = "220328185654-cubone-brock1win.txt"

event_text = get_text(filenames_text_formatted)
event_text_formatted = text_format(event_text)

move_critability_info = get_text('critical_moves.txt')
move_critability_info_formatted = text_format(move_critability_info)

for i in range(len(event_text_formatted)):
    nickname = 'CRY'
    if nickname in event_text_formatted[i]:
        swap_words_in_line('CRY', 'CUBONE', event_text_formatted[i])

event_index = get_event_index(event_text_formatted)

accuracy_event_list = get_accuracy_event_list(event_text_formatted, event_index, move_info_formatted)
critical_event_list = get_critical_event_list(event_text_formatted,
                                              event_index,
                                              base_stats_formatted,
                                              move_info_formatted,
                                              move_critability_info_formatted)
# effect_event_list = get_effect_event_list(event_text_formatted,event_index,move_info_formatted)

event_list = get_event_list(accuracy_event_list, critical_event_list)

good_event_list = get_good_event_list(event_list)
bad_event_list = get_bad_event_list(event_list)


good_surprise = get_surpise(good_event_list)
bad_surprise = get_surpise(bad_event_list)

print(good_surprise - bad_surprise, '\t', filenames_text_formatted, '\n')

    # x = good_event_list
    # for i in range(len(x)):
    #     print(event_text_formatted[x[i].index_num], x[i].goodness_bool, x[i].probability, x[i].justification, sep='\t')
    #
    # y = bad_event_list
    # for i in range(len(y)):
    #     print(event_text_formatted[y[i].index_num], y[i].goodness_bool, y[i].probability, y[i].justification, sep='\t')


