# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-23T15:28:58.957772+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CVX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.164 | entrée 5.750 | trend 8.350 | rang 6.815
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CVX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.815
2. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.718
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.672

## Accélération indépendante

- BIRB-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 8.160/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — CONFIRMED_ACCELERATION — score 7.743/10 — DETECTED_BUT_TOO_LATE
- CTR-EUR — BUILDING_ACCELERATION — score 6.435/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 6.351/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 6.146/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARKM-EUR — BUILDING_ACCELERATION — score 5.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PARTI-EUR — BUILDING_ACCELERATION — score 4.790/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 8.820/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IRYS-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- UP-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EPIC-EUR — MEMORY_24H — score mémoire 8.032/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.921/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 7.743/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- VELO-EUR — MEMORY_24H — score mémoire 7.742/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.722/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.699/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +155.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +41.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +28.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +24.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +21.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +12.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEPE-EUR +10.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +9.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +9.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +9.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
