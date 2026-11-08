# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-08T15:47:26.258116+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BIRB-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.054 | entrée 3.850 | trend 8.650 | rang 6.821
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.821
2. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.458
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.225

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.694/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — BUILDING_ACCELERATION — score 5.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEGEN-EUR — BUILDING_ACCELERATION — score 5.744/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 5.437/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — BUILDING_ACCELERATION — score 5.394/10 — DETECTED_BUT_TOO_LATE
- O-EUR — BUILDING_ACCELERATION — score 4.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 9.403/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.877/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 8.694/10 — sources ACCELERATION — WATCH_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.777/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — MEMORY_DECAY_24_72H — score mémoire 7.251/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.245/10 — sources V4 — WATCH_ONLY
- INJ-EUR — MEMORY_24H — score mémoire 7.048/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BLEND-EUR — MEMORY_24H — score mémoire 6.827/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — ACTIVE_NOW — score mémoire 6.821/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.485/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HOT-EUR +18.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- DGB-EUR +10.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RSR-EUR +9.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BOB-EUR +8.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +6.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CAP-EUR +6.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SIGN-EUR +6.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEGA-EUR +5.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MAVIA-EUR +5.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +4.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
