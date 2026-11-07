# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-07T02:06:57.080180+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.715 | entrée 6.150 | trend 7.600 | rang 6.464
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.464
2. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.304

## Accélération indépendante

- CARV-EUR — CONFIRMED_ACCELERATION — score 9.061/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — CONFIRMED_ACCELERATION — score 8.929/10 — DETECTED_BUT_TOO_LATE
- STO-EUR — BUILDING_ACCELERATION — score 5.267/10 — DETECTED_BUT_TOO_LATE
- RECALL-EUR — BUILDING_ACCELERATION — score 4.972/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 9.777/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.163/10 — sources ACCELERATION — MEMORY_ONLY
- CARV-EUR — ACTIVE_NOW — score mémoire 9.061/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- 2Z-EUR — ACTIVE_NOW — score mémoire 8.929/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PTB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.439/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 7.098/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 6.906/10 — sources ACCELERATION — MEMORY_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 6.775/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +33.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +23.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +20.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +19.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAVIA-EUR +11.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +10.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SLX-EUR +10.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MANTRA-EUR +10.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FLOCK-EUR +9.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAFE-EUR +9.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
