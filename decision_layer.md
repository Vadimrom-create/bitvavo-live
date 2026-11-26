# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-26T20:18:29.423791+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BLUR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.889 | entrée 6.250 | trend 7.950 | rang 6.631
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BLUR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.631
2. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.430

## Accélération indépendante

- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.291/10 — DETECTED_BUT_TOO_LATE
- KNTQ-EUR — CONFIRMED_ACCELERATION — score 7.144/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.848/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDP-EUR — BUILDING_ACCELERATION — score 6.012/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — BUILDING_ACCELERATION — score 5.187/10 — DETECTED_BUT_TOO_LATE
- DODO-EUR — BUILDING_ACCELERATION — score 5.102/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 4.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INIT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- THQ-EUR — MEMORY_DECAY_24_72H — score mémoire 9.710/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_DECAY_24_72H — score mémoire 9.414/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 8.993/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — ACTIVE_NOW — score mémoire 7.291/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — MEMORY_24H — score mémoire 7.242/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — ACTIVE_NOW — score mémoire 7.199/10 — sources V4 — WATCH_ONLY
- KNTQ-EUR — ACTIVE_NOW — score mémoire 7.144/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TAI-EUR — ACTIVE_NOW — score mémoire 6.848/10 — sources ACCELERATION — WATCH_ONLY
- KITE-EUR — MEMORY_DECAY_24_72H — score mémoire 6.658/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NES-EUR +25.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KNTQ-EUR +24.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SEI-EUR +21.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +21.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SSV-EUR +21.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTC-EUR +16.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ME-EUR +14.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LRC-EUR +13.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKY-EUR +12.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIF-EUR +11.11% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
