class Event:  # an event is a set of outcomes of an experiment (a subset of the sample space) to which a probability is assigned
    def __init__(self, index_num, ally_bool, pokemon_species, justification, goodness_bool=True, probability=1):
        self.index_num = index_num
        self.ally_bool = ally_bool
        self.pokemon_species = pokemon_species
        self.justification = justification
        self.goodness_bool = goodness_bool
        self.probability = probability


class AccuracyEvent(Event):
    def __init__(self, index_num, ally_bool, pokemon_species, justification, goodness_bool, probability,
                 move_accuracy=100,
                 opposing_evasion_level=0,
                 accuracy_level=0,
                 infatuation_bool=False,
                 paralysis_bool=False,
                 confusion_bool=False,
                 hit_bool=True):
        super().__init__(index_num, ally_bool, pokemon_species, justification, goodness_bool, probability)
        self.move_accuracy = move_accuracy
        self.opposing_evasion_level = opposing_evasion_level
        self.accuracy_level = accuracy_level
        self.infatuation_bool = infatuation_bool
        self.paralysis_bool = paralysis_bool
        self.confusion_bool = confusion_bool
        self.hit_bool = hit_bool


class CriticalEvent(Event):
    def __init__(self, index_num, ally_bool, pokemon_species, justification, goodness_bool, probability,
                 pokemon_speed=100, high_crit_rate=False, crit_chance=0, critical_bool=False):
        super().__init__(index_num, ally_bool, pokemon_species, justification, goodness_bool, probability)
        self.pokemon_speed = pokemon_speed
        self.high_crit_rate = high_crit_rate
        self.crit_chance = crit_chance
        self.critical_bool = critical_bool


class EffectEvent(Event):
    def __init__(self, index_num, ally_bool, pokemon_species, justification, goodness_bool, probability,
                 effect_chance=0, effect_keyword='', effect_bool=False):
        super().__init__(index_num, ally_bool, pokemon_species, justification, goodness_bool, probability)
        self.effect_chance = effect_chance
        self.effect_keyword = effect_keyword
        self.effect_bool = effect_bool
