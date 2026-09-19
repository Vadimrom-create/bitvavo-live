# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T17:16:06.516238+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.619 | entrée 8.200 | trend 8.750 | rang 8.297
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.458 | entrée 4.500 | trend 8.050 | rang 7.013
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.985 | entrée 6.500 | trend 8.550 | rang 7.120
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.297
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.725
3. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.305

## Accélération indépendante

- PEPE-EUR — BUILDING_ACCELERATION — score 5.964/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 4.953/10 — DETECTED_BUT_TOO_LATE
- DOGE-EUR — BUILDING_ACCELERATION — score 4.948/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 4.917/10 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — BUILDING_ACCELERATION — score 4.792/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HYPE-EUR — ACTIVE_NOW — score mémoire 8.297/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.291/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.096/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.916/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +45.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +27.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +27.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +27.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +24.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +21.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +20.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +19.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +19.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
