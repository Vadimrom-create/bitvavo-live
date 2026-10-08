# Volume relatif / capitalisation — shadow causal V1

Chantier #134. **Mesure seule, aucun veto, aucun signal ACHÈTE et aucune modification HUMAN SWING.**

## Ce qui fonctionne déjà
Le fichier public `bitvavo_live.json` donne, pour chaque paire suivie :
- `quote_volume_24h_eur` **Bitvavo seulement** ;
- `m15.volume_last_vs_prev20` : volume de la dernière bougie 15 min vs moyenne de 20 précédentes ;
- `m15.volume_4_vs_prev4` : dernière heure vs heure précédente ;
- `m15.volume_16_vs_prev16` : quatre dernières heures vs quatre heures précédentes ;
- `spread_pct` : spread *instantané*, non synonyme de carnet exécutable.

L'outil `scripts/scan_volume_turnover_shadow.py` lit ces données et conserve TOUS les marchés observés, y compris sans hausse ou sans capitalisation connue. Il ne classe jamais un score de volume comme une probabilité de hausse.

## Formule et alignement temporel

`turnover_bitvavo_24h_pct = 100 * volume_24h_bitvavo_eur / cap_eur`

`turnover_global_24h_pct = 100 * volume_24h_global_eur / cap_eur`

Les deux ratios ont un **numérateur différent** ; ils ne doivent jamais être présentés comme la même chose. Le volume global doit venir du **même fournisseur** et du **même horodatage** que la capitalisation. Aucun fournisseur de cap n'est encore branché en production.

### Entretien d'une identité vérifiée
La commande accepte un fichier facultatif JSON contenant une ligne par marché (exemple FICTIF) :

```json
{"rows":[{"market":"DEMO-EUR","asset_id":"verified-provider-asset-id","identity_verified":true,"market_cap_eur":10000000,"global_volume_24h_eur":1500000,"source":"verified-provider","asof_utc":"2026-10-08T20:45:00Z"}]}
```

L'`asset_id` doit être **relié manuellement au bon token et contrôlé** au préalable, notamment lorsqu'un symbole existe sur plusieurs réseaux. Les sources qui s'identifient uniquement par `OGN`, `RLC` ou `ZRC` sans identifiant d'actif ne sont pas admissibles. Une capitalisation absente, non vérifiée, plus récente que le scan (*lookahead*), vieille de plus de 24h ou invalide est systématiquement écartée et son absence est reportée.

## Exécution sans toucher à la production

```bash
python scripts/scan_volume_turnover_shadow.py --live bitvavo_live.json --output /tmp/volume_turnover_shadow.json
# Avec source de cap identifiée et horodatée, facultative :
python scripts/scan_volume_turnover_shadow.py --live bitvavo_live.json --marketcap /tmp/verified_caps.json --output /tmp/volume_turnover_shadow_with_caps.json
```

La CI exécute les tests et produit un **artefact de diagnostic** basé sur la photographie Bitvavo disponible. Tant qu'aucun cap n'est fourni, `cap_coverage_pct=0` est le résultat **correct**, plutôt qu'un ratio inventé. Les signaux et carnets du moment doivent ensuite être vérifiés séparément ; ce script ne mesure pas une taille d'ordre réellement remplissable.

## Prérequis avant d'affirmer une valeur prédictive

1. Source machine vérifiée des capitalisations, historique archivage sans altération et identifiants d'actifs persistants.
2. Mesures prospectives **avant la hausse**, pas sélection ex post des gagnants OGN/RLC/ZRC.
3. Comparer des *épisodes indépendants* de toutes tailles et régimes de marché, avec chronologie, coûts et trades plausibles.
4. Comparaison hors échantillon volume seul / turnover + RVOL / référence Solaire / ChatGPT, mêmes horizons et gestion des sorties.
5. Après maturité 24/48/72 h et 7 j, ne promouvoir une règle que si elle augmente le résultat net robuste sans accroître de façon indue les faux signaux.

L'outil est un **premier instrument de mesure** et non le backtest exhaustif. Les deux projets HUMAN SWING et God Layer restent dans leur état initial (HUMAN SWING prioritaire, God Layer en pause).
