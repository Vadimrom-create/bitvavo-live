# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T10:29:06.440495+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : USELESS-EUR | action LATENT_ACCELERATOR | opportunité 7.446 | entrée 5.750 | trend 8.100 | rang 6.530
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.002 | entrée 8.000 | trend 8.100 | rang 7.379
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.379
2. USELESS-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.530

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.446/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 6.285/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.454/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.275/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +113.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +44.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALIGN-EUR +21.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +18.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +17.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +15.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +15.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- G-EUR +11.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +7.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +6.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
