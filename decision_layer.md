# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-27T03:02:22.733766+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.819 | entrée 5.750 | trend 7.900 | rang 6.579
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.579
2. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.546

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- INIT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.896/10 — sources ACCELERATION — MEMORY_ONLY
- THQ-EUR — MEMORY_DECAY_24_72H — score mémoire 8.326/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_DECAY_24_72H — score mémoire 8.073/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.291/10 — sources ACCELERATION — MEMORY_ONLY
- AIXBT-EUR — MEMORY_24H — score mémoire 7.242/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 7.199/10 — sources V4 — MEMORY_ONLY
- KNTQ-EUR — MEMORY_24H — score mémoire 7.144/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 6.848/10 — sources ACCELERATION — MEMORY_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 6.631/10 — sources DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- KNTQ-EUR +43.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SSV-EUR +21.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LRC-EUR +20.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +17.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +16.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIGTIME-EUR +14.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +13.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKY-EUR +12.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +12.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SEI-EUR +12.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
