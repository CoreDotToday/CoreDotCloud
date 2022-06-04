from elasticsearch import Elasticsearch


def get_client_es(host="http://localhost", http_auth=(), port=9200):
    """get ElasticSearch Client

    Parameters
    ----------
    host : str, optional
        es host, by default "http://localhost:9200"
    http_auth : tuple, optional
        id, pw, by default ()
    port : int, optional
        es port, by default 9200

    Returns
    -------
    elasticsearch.client.Elasticsearch
        client
    """

    es = Elasticsearch([host], http_auth=http_auth, port=port)
    return es


# def es_search(es, index, body, sort, _size, _from):
#     """Search for elasticsearch

#     Parameters
#     ----------
#     es : _type_
#         _description_
#     index : _type_
#         _description_
#     body : _type_
#         _description_
#     sort : _type_
#         _description_
#     _size : _type_
#         _description_
#     _from : _type_
#         _description_

#     Returns
#     -------
#     _type_
#         ```{'took': 1,
#         'timed_out': False,
#         '_shards': {'total': 50, 'successful': 50, 'skipped': 0, 'failed': 0},
#         'hits': {'total': {'value': 0, 'relation': 'eq'},
#         'max_score': None,
#         'hits': []}}```
#     """
#     result = es.search(index=index,
#                        body=body,
#                        sort=sort,
#                        size=_size,
#                        from_=_from
#                        )
#     return result
