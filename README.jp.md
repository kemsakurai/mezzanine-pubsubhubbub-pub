mezzanine_pubsubhubbub_pub
==========================

[![Build Status](https://travis-ci.org/kemsakurai/mezzanine-pubsubhubbub-pub.svg?branch=master)](https://travis-ci.org/kemsakurai/mezzanine-pubsubhubbub-pub)

mezzanine_pubsubhubbub_pub は python django を基に作られた CMS である mezzanine で、  
pubsubhubbub の publish 通知を行う 拡張プラグインです。  
django の pubsubhubbub プラグイン [brutasse/django-push: PubSubHubbub support for Django](https://github.com/brutasse/django-push)  
を参考に作成しています。  

必要条件
======================

以下のパッケージインストールを必須としています。<sup>[1](#note1)</sup>  
<small id="note1">pip install 時にインストールされるパケージの事です。</small>  
バージョン指定なしのため、最新版がインストールされます。  

* mezzanine 
* requests 
* mock (テスト実行時に必要)

インストール
======================
```console
pip install mezzanine_pubsubhubbub_pub
```

設定
======================
* settings.py に アプリケーションを追加します。  

```python
INSTALLED_APPS = (
    "mezzanine_pubsubhubbub_pub",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.generic",
......

```

* urls.py に以下の記述を追加します。  
```python
from mezzanine_pubsubhubbub_pub import get_feed_url_patterns
urlpatterns += get_feed_url_patterns()
```
これは、mezzanine.blog の url をinclude する前に追加する必要があります。<sup>[1](#note2)</sup>  
<small id="note2">mezzanine。blog の url の設定を上書きするためです。 </small>  

* settings.py に PUSH_HUB の設定をする    
HUBサーバーの設定を行います。
デフォルト値は、```("https://pubsubhubbub.appspot.com/",)``` です。  
Taple で 複数URL 設定が可能です。  
管理画面では編集は不可になります。  

* settings.py に PUSH_URL_PROTOCOL の設定をする  

通知時に知らせるFeed URL のプロトコルを設定します。  
HTTP_ONLY, HTTPS_ONLY, BOTH が設定可能で、  
BOTH は HTTP/HTTPS 双方のFeed URLで通知を行います。  
デフォルト値は、HTTP_ONLY になり、  
管理画面での編集が可能です。  


これで設定は終わりです。  

TODO
====
* 下位Version に対してのサポート

* 柔軟なFeed URL 設定

* Batch Job 作成  

等。 個人ではあまり思い浮かばないので、是非issue登録と、pull requestを!!!

