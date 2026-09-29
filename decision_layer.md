# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T08:25:15.147775+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.899 | entrée 7.850 | trend 9.200 | rang 8.206
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.555 | entrée 6.700 | trend 7.500 | rang 7.213
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : C-EUR | action LATENT_ACCELERATOR | opportunité 7.452 | entrée 4.500 | trend 8.250 | rang 7.121
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XLM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.422 | entrée 8.150 | trend 8.750 | rang 8.343
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.206 — opportunité 8.899 — entrée 7.850 — trend 9.200
2. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.858 — opportunité 8.615 — entrée 6.800 — trend 8.100
3. APT-EUR — ACHETE_MAINTENANT — rank 7.260 — opportunité 8.501 — entrée 7.000 — trend 6.750
4. ADA-EUR — ACHETE_MAINTENANT — rank 7.167 — opportunité 8.784 — entrée 7.450 — trend 6.100
5. TAO-EUR — ACHETE_MAINTENANT — rank 6.825 — opportunité 7.980 — entrée 7.200 — trend 6.300

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.343
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.206
3. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.066

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 9.052/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — CONFIRMED_ACCELERATION — score 8.690/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — CONFIRMED_ACCELERATION — score 8.484/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 8.254/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — CONFIRMED_ACCELERATION — score 7.793/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — CONFIRMED_ACCELERATION — score 7.641/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BANANA-EUR — CONFIRMED_ACCELERATION — score 7.627/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.287/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — CONFIRMED_ACCELERATION — score 7.196/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GALA-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- UNI-EUR — ACTIVE_NOW — score mémoire 6.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 9.052/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 8.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +38.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +32.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +21.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +19.74% — DETECTED_EARLY — couche NONE — action NONE
- CELO-EUR +17.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +16.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +14.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +14.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +14.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICP-EUR +14.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
