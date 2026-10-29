# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-29T00:08:02.288473+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 8.026 | entrée 7.700 | trend 9.000 | rang 7.627
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.069 | entrée 6.000 | trend 8.150 | rang 6.858
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

1. PEPE-EUR — ACHETE_MAINTENANT — rank 7.627 — opportunité 8.026 — entrée 7.700 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.627
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.858
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.855

## Accélération indépendante

- QUID-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 6.200/10 — DETECTED_BUT_TOO_LATE
- PEPE-EUR — BUILDING_ACCELERATION — score 6.095/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.180/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 4.892/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLEND-EUR — BUILDING_ACCELERATION — score 4.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPX-EUR — BUILDING_ACCELERATION — score 4.817/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CELO-EUR — MEMORY_24H — score mémoire 7.853/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — MEMORY_24H — score mémoire 7.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.185/10 — sources ACCELERATION — MEMORY_ONLY
- BABY-EUR — MEMORY_24H — score mémoire 7.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 7.000/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- XMN-EUR +92.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +35.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +33.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +26.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XAN-EUR +17.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +14.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +14.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +11.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BICO-EUR +10.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +7.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
