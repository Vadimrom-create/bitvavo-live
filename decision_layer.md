# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T06:03:16.352721+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XVG-EUR | action ACHETE_MAINTENANT | opportunité 9.209 | entrée 7.450 | trend 8.200 | rang 8.230
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MMT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.963 | entrée 6.150 | trend 8.200 | rang 8.012
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOMI-EUR | action LATENT_ACCELERATOR | opportunité 9.166 | entrée 5.750 | trend 8.100 | rang 8.050
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.158 | entrée 6.700 | trend 8.950 | rang 8.368
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XVG-EUR — ACHETE_MAINTENANT — rank 8.230 — opportunité 9.209 — entrée 7.450 — trend 8.200
2. AAVE-EUR — ACHETE_MAINTENANT — rank 7.995 — opportunité 8.562 — entrée 7.250 — trend 8.700
3. PUMP-EUR — ACHETE_MAINTENANT — rank 7.919 — opportunité 9.243 — entrée 7.000 — trend 8.250
4. AERO-EUR — ACHETE_MAINTENANT — rank 7.918 — opportunité 9.147 — entrée 7.250 — trend 7.750
5. XDC-EUR — ACHETE_MAINTENANT — rank 7.840 — opportunité 8.280 — entrée 6.900 — trend 8.700
6. NEAR-EUR — ACHETE_MAINTENANT — rank 7.621 — opportunité 8.145 — entrée 7.950 — trend 8.300
7. ENA-EUR — ACHETE_MAINTENANT — rank 7.618 — opportunité 8.171 — entrée 7.150 — trend 8.650
8. ALGO-EUR — ACHETE_MAINTENANT — rank 7.486 — opportunité 7.800 — entrée 6.950 — trend 8.150
9. FET-EUR — ACHETE_MAINTENANT — rank 7.485 — opportunité 8.221 — entrée 7.900 — trend 7.550
10. TAO-EUR — ACHETE_MAINTENANT — rank 7.161 — opportunité 7.890 — entrée 7.300 — trend 7.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.368
2. XVG-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.230
3. ZIG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.181

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 9.090/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 8.988/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.575/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — CONFIRMED_ACCELERATION — score 7.522/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 7.107/10 — DETECTED_BUT_TOO_LATE
- KAIA-EUR — BUILDING_ACCELERATION — score 5.987/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.360/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — BUILDING_ACCELERATION — score 4.939/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — ACTIVE_NOW — score mémoire 9.090/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SYN-EUR — ACTIVE_NOW — score mémoire 8.988/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.368/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.346/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.230/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.181/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- MOVR-EUR +84.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +44.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +28.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +28.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +26.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRAC-EUR +26.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +21.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOM-EUR +16.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ESP-EUR +14.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PLUME-EUR +14.24% — DETECTED_EARLY — couche NONE — action NONE

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
