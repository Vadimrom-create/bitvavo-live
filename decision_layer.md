# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-07T15:12:24.665963+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BIRB-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.906 | entrée 5.450 | trend 8.300 | rang 6.819
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.819
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.438

## Accélération indépendante

- DEGEN-EUR — BUILDING_ACCELERATION — score 6.474/10 — DETECTED_BUT_TOO_LATE
- THE-EUR — BUILDING_ACCELERATION — score 6.379/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 4.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ELSA-EUR — BUILDING_ACCELERATION — score 4.920/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — BUILDING_ACCELERATION — score 4.766/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 9.777/10 — sources ACCELERATION — MEMORY_ONLY
- CARV-EUR — MEMORY_24H — score mémoire 9.061/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.929/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 7.602/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 7.540/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 7.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 7.098/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 6.906/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- DEGEN-EUR +37.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EPIC-EUR +29.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +21.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +8.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +8.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MET-EUR +8.23% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ACT-EUR +8.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TAI-EUR +6.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BLEND-EUR +6.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SWELL-EUR +6.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
