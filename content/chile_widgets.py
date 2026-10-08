"""The scenario widget for the Chile macro-fiscal model.

The sliders are the five shocks of chile_scenarios.ipynb, one tab each. A notebook only needs::

    from chile_widgets import scenario_widget
    scenario_widget(mchile)

All sliders act on the model's period (``mchile.current_per``), so a shock starts in its first
year.
"""

from modelwidget_input import make_widget, updatewidget


def slidedefs(health_el=0.66):
    """The tab definition: one slide definition per shock. ``health_el`` is the baseline
    health elasticity, the health slider's starting value."""

    vat_slidedef = ['slide', {
        'heading': 'VAT rate, share',
        'content': {
            'VAT rate, change': {'var': 'TAU_CONS', 'value': 0.0, 'min': -0.05, 'max': 0.05,
                                 'step': 0.005, 'dec': 3, 'op': '+'},
        }
    }]

    pension_slidedef = ['slide', {
        'heading': 'Pension spending, share of GDP',
        'content': {
            # G_P_STEP is added to the pension share once and stays in it, so only in the first year
            'Pension spending, permanent step': {'var': 'G_P_STEP', 'value': 0.0, 'min': -0.01, 'max': 0.02,
                                                 'step': 0.001, 'dec': 3, 'op': '+impulse'},
        }
    }]

    health_slidedef = ['slide', {
        'heading': 'Health spending',
        'content': {
            'Elasticity to the 80+ share': {'var': 'HEALTH_EL', 'value': health_el, 'min': 0.3, 'max': 1.0,
                                            'step': 0.01, 'op': '='},
        }
    }]

    female_slidedef = ['slide', {
        'heading': 'Participation rate, women 15-59, share',
        'content': {
            'Participation rate, change': {'var': 'P_F_1559', 'value': 0.0, 'min': -0.1, 'max': 0.15,
                                           'step': 0.01, 'op': '+'},
        }
    }]

    copper_slidedef = ['slide', {
        'heading': 'Copper price',
        'content': {
            'Steady-state copper price, % change': {'var': 'PCOPPER_SS', 'value': 0.0, 'min': -50, 'max': 50,
                                                    'step': 5, 'dec': 0, 'op': '%'},
        }
    }]

    return ['tab', {
        'content': [
            ('VAT',                  vat_slidedef),
            ('Pensions',             pension_slidedef),
            ('Health',               health_slidedef),
            ('Female participation', female_slidedef),
            ('Copper',               copper_slidedef),
        ]
    }]


def scenario_widget(mmodel):
    """The sliders with the run buttons and a viewer of the kept solutions, the baseline
    being the model's data (``mmodel.basedf``)."""
    health_el = mmodel.basedf.loc[mmodel.current_per[0], 'HEALTH_EL']
    winput = make_widget(slidedefs(health_el))
    return updatewidget(mmodel, winput, basename='Baseline',
                        selectfrom='B_G REV_TOT G_TOT G_P_NOM_GDP G_H_NOM_GDP REV_C PIBREAL_TOT LAB_MAR',
                        selected='B_G')
