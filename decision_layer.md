# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-30T23:23:23.764027+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.925 | entrée 4.750 | trend 7.900 | rang 6.539
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.539

## Accélération indépendante

- RECALL-EUR — CONFIRMED_ACCELERATION — score 9.168/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.637/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.021/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — CONFIRMED_ACCELERATION — score 6.795/10 — DETECTED_BUT_TOO_LATE
- ILV-EUR — BUILDING_ACCELERATION — score 6.363/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 5.702/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — BUILDING_ACCELERATION — score 5.418/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WOO-EUR — BUILDING_ACCELERATION — score 5.403/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.147/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 5.033/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RECALL-EUR — ACTIVE_NOW — score mémoire 9.168/10 — sources ACCELERATION — WATCH_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.661/10 — sources ACCELERATION — MEMORY_ONLY
- TRX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.306/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 7.637/10 — sources ACCELERATION — WATCH_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 7.021/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PEPE-EUR — MEMORY_24H — score mémoire 6.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 6.844/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 6.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- BEAM-EUR +39.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +36.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GWEI-EUR +22.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +16.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OP-EUR +16.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WOO-EUR +15.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRC-EUR +15.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +14.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +14.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUNDIX-EUR +12.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
