# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T18:55:28.515978+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.457 | entrée 7.650 | trend 8.900 | rang 8.487
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.386 | entrée 5.850 | trend 8.950 | rang 7.955
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JTO-EUR | action LATENT_ACCELERATOR | opportunité 8.936 | entrée 5.650 | trend 8.750 | rang 8.114
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.433 | entrée 7.800 | trend 8.850 | rang 8.369
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.487
2. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.411
3. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.369

## Accélération indépendante

- ENA-EUR — CONFIRMED_ACCELERATION — score 7.741/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUDIO-EUR — CONFIRMED_ACCELERATION — score 7.093/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — BUILDING_ACCELERATION — score 5.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — BUILDING_ACCELERATION — score 5.665/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — BUILDING_ACCELERATION — score 5.412/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RPL-EUR — BUILDING_ACCELERATION — score 5.411/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 5.361/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 5.191/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — BUILDING_ACCELERATION — score 5.014/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 4.876/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CC-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ENA-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.487/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.411/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.369/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ATH-EUR — ACTIVE_NOW — score mémoire 8.348/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +55.08% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +46.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +31.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +28.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INX-EUR +26.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +20.48% — DETECTED_EARLY — couche NONE — action NONE
- GLMR-EUR +19.71% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +17.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +14.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +13.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
