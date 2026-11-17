# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-16T23:59:07.451177+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.366 | entrée 4.550 | trend 7.600 | rang 6.210
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.210

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 9.204/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HFT-EUR — ACTIVE_NOW — score mémoire 9.204/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ASTER-EUR — MEMORY_DECAY_24_72H — score mémoire 7.349/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 7.254/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 7.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.926/10 — sources V4 — MEMORY_ONLY
- HNT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.708/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 6.696/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 6.287/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.210/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- GLMR-EUR — MEMORY_DECAY_24_72H — score mémoire 6.122/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HUMA-EUR +50.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CROSS-EUR +30.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +25.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +14.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICP-EUR +12.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +12.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ASTER-EUR +10.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +10.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RARE-EUR +7.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REQ-EUR +7.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
