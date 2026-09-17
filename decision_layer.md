# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T11:21:33.847962+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.788 | entrée 6.550 | trend 8.100 | rang 6.785
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.785

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.770/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.626/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SOMI-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.113/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.031/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.780/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +81.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +31.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +23.37% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- COTI-EUR +18.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +17.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +17.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +15.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +15.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDEN-EUR +13.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +13.33% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
