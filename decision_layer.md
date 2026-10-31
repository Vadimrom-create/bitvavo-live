# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-31T02:33:42.913603+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.118 | entrée 4.800 | trend 8.000 | rang 6.730
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.730
2. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.712
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.706

## Accélération indépendante

- ELSA-EUR — CONFIRMED_ACCELERATION — score 6.586/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RECALL-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.661/10 — sources ACCELERATION — MEMORY_ONLY
- TRX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.741/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.637/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.397/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 7.021/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 6.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_DECAY_24_72H — score mémoire 6.750/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 6.730/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- BEAM-EUR +46.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HFT-EUR +40.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +33.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +23.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +21.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OP-EUR +19.74% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- U-EUR +19.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GWEI-EUR +19.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CFG-EUR +18.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +17.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
