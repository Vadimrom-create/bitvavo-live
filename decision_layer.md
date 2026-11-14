# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-14T11:09:04.636120+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CAP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.523 | entrée 6.100 | trend 7.850 | rang 6.477
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.477

## Accélération indépendante

- DODO-EUR — CONFIRMED_ACCELERATION — score 6.676/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.197/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 7.598/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 7.492/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 7.091/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.676/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SXT-EUR — MEMORY_24H — score mémoire 6.517/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.478/10 — sources V4 — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 6.477/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- 0G-EUR — MEMORY_24H — score mémoire 6.209/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 6.197/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 6.070/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SHELL-EUR +57.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +20.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BOB-EUR +10.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +8.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +5.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LMWR-EUR +5.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HFT-EUR +4.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AGI-EUR +3.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +3.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- XDP-EUR +3.55% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
