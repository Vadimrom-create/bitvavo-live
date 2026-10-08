# Contrat SCAN / responsabilité ChatGPT — v1

Statut : **mesure et discipline décisionnelle**, aucune modification des règles de trading. Priorité HUMAN SWING. God Layer en pause. Chantiers : issue #134.

## Principe
Un refus ChatGPT n'est **jamais** un veto machine définitif. Il constitue une recommandation contextualisée et révisable. Une nouvelle alerte Solaire, un changement de spread/carnet/liquidité, un niveau atteint ou un changement macro force un nouvel arbitrage. L'utilisateur ne doit pas devoir retrouver les hausses manquées ou demander lui-même un suivi.

À chaque SCAN :
1. Relever heure UTC + fuseau, versions / identifiant du cycle, date de collecte et fraîcheur. Séparer le live du cache. Si les prix/carnets ne sont pas accessibles ou frais, indiquer `EXÉCUTION NON VALIDÉE` ; ne pas inventer.
2. **Big picture** : calendrier macro des prochaines 72h (heure locale, source, importance), décisions attendues, BTC/ETH, régime des altcoins, risque de fenêtre d'annonce. Distinguer faits, scénarios et inconnues. La macro n'est pas un veto automatique hors politique justifiée.
3. Construire l'union (a) signaux Solaire présents, (b) alertes ACHÈTE récentes, (c) mémoire 72h et rejets, (d) nouvelle accélération + changement liquidité, (e) leaderboard actuel. Ne pas écarter un candidat du simple fait qu'il ne figure pas dans le top N du dernier scan.
4. Pour au maximum trois candidats : structure et score Solaire, volume 15m/1h/24h **comparé à sa normale**, volume global et volume Bitvavo distingués, capitalisation flottante et son timestamp, ratio volume global/cap (si valeurs réellement disponibles), spread, carnet bid/ask, prix moyen et slippage aller/retour simulés à 100€ et 150€, stop structurel, potentiel net restant, déduplication d'épisode, information NEWS/catalyseurs.
5. Produire une décision explicite : `ACHAT_VALIDÉ_SOUMIS_A_EXECUTION`, `ATTENTE_RÉÉVALUATION`, `REFUS_STRUCTUREL`, `INCONNU_DONNEES_INSUFFISANTES`. Justifier la contradiction si ChatGPT refuse une alerte machine ACHÈTE et indiquer **quelle donnée vérifiable** ferait changer d'avis.
6. Retenir les refus pour réexamen sur événement, non pas dans une « liste noire ». Reporter spontanément tout ancien signal validé qui a accéléré et attribuer détection / exécution / arbitrage sans hindsight.

## Ligne de décision privée minimale (un événement par décision)
Journal append-only, horodaté, format JSONL suggéré. **Ne pas publier en clair dans ce dépôt public** les données de portefeuille, transactions réelles, montants personnels, emails ou discussions privées.

| Champ | Exigence |
|---|---|
| `scan_id, decided_at_utc, source_scan_id, source_commit, data_asof_utc` | Traçabilité et fraîcheur |
| `market, candidate_episode_id, source_signal, source_action, source_score` | Cause d'entrée observable |
| `chatgpt_action, chatgpt_reason_codes, evidence_uris` | Ce que ChatGPT a décidé et pourquoi |
| `market_regime, macro_window, news_catalyst_known` | Contexte daté, pas réécrit ex post |
| `volume_global_24h_eur, volume_bitvavo_24h_eur, market_cap_eur, turnover_global_24h, relative_volume_15m, relative_volume_1h, relative_volume_24h` | Numérateur, dénominateur, marché et horodatage explicites ; manquant = null |
| `spread_pct, depth_bid_1pct_eur, depth_ask_1pct_eur, simulated_roundtrip_100eur_pct, simulated_roundtrip_150eur_pct, book_asof_utc` | Faisabilité d'un ordre réel de taille modeste |
| `entry_kind, entry_limit_eur, stop_eur, tp_eur, expected_fee_slippage_pct` | Plan vérifiable ex ante |
| `recheck_trigger, recheck_deadline_utc, supersedes_decision_id` | Continuité après un refus |
| `execution_source, actual_fill_status` | Source privée distincte ; null si inconnu |

**Pas de stockage public automatique du journal.** Avant de chiffrer la contribution de ChatGPT, définir et tester un stockage privé et une méthode de capture fiable des recommandations issues du chat. Une page Markdown n'est PAS un pipeline de capture.

## Cadre de comparaison
Cohortes appariées `SOLAIRE_SEUL`, `SOLAIRE+CHATGPT`, `HUMAN_SWING_R2`, même univers, heure, capital / exposition maximum, frais, profondeur, politique de stop/TP et événements macro. Comparer les résultats **nets** sur 4 h/24 h/48 h/72 h/7 j et les événements indépendants ; rendre le nombre maturé et la censure explicites.

Pertes évitées et gains abandonnés : contrefactuels uniquement si une entrée aurait pu être remplie et si son trajet jusqu'au stop/TP est observable. Le maximum futur d'une bougie n'est jamais un PnL réalisé. Utiliser `NON_MESURABLE` si les journaux ou la liquidité historique manquent.

Variables (turnover, RVOL, etc.) : **diagnostics shadow uniquement**, aucune pondération optimisée sur OGN/RLC/ZRC vus a posteriori. Évaluer aussi les actifs sans hausse et les faux positifs.

## Critères pour clore #134
- Décisions traçables avec 100 % d'horodatages et références de source sur la cohorte test ; refus suivis/réévalués.
- Comparaison économique auditable, ou défaut de données explicitement qualifié `NON_MESURABLE`.
- Bilan hebdomadaire cumulatif, avec maturité, N, PnL et divergences, et alertes exceptionnelles en cas de défaut critique.
- Temps humain mesuré de manière non intrusive (début/fin de session, relances), sans imputer une durée fictive.
- Pas de validation de supériorité sans échantillon indépendant et absence de fuite du futur.
