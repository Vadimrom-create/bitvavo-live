# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-29T05:25:19.736603+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 7.860 | entrée 7.850 | trend 9.000 | rang 7.623
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.337 | entrée 6.350 | trend 8.400 | rang 7.190
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

1. PEPE-EUR — ACHETE_MAINTENANT — rank 7.623 — opportunité 7.860 — entrée 7.850 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.623
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.190
3. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.016

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 8.747/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — CONFIRMED_ACCELERATION — score 7.846/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALIGN-EUR — CONFIRMED_ACCELERATION — score 7.716/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.713/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.580/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 6.876/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 5.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.447/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — BUILDING_ACCELERATION — score 5.400/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HOME-EUR — BUILDING_ACCELERATION — score 5.368/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.623/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — ACTIVE_NOW — score mémoire 8.747/10 — sources ACCELERATION — WATCH_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CELO-EUR — MEMORY_24H — score mémoire 7.853/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources ACCELERATION — WATCH_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources ACCELERATION — WATCH_ONLY
- CNPY-EUR — ACTIVE_NOW — score mémoire 7.713/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- XMN-EUR +58.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +22.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +21.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +18.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +15.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +14.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +12.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +8.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +8.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +7.56% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
