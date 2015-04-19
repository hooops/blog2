<!DOCTYPE html>
<!-- saved from url=(0048)http://v3.bootcss.com/examples/navbar-fixed-top/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <!--link rel="icon" href="http://v3.bootcss.com/favicon.ico" -->

    <title>MyBlog</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/navbar-fixed-top.css" rel="stylesheet">
    <link href="/static/css/customize.css" rel="stylesheet">

  </head>

  <body>

    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container ">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" a href="/index/">MyBlog</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">个人主页</a></li>
            {% for category in bbs_category%}
               
                {% ifequal category.id  cata_id %}
                    <li class="active"><a href="/category/{{category.id}}/">{{category.name}}</a></li>
                {%else%}
                     <li class=""><a href="/category/{{category.id}}/">{{category.name}}</a></li>
                {%endifequal%}
            {%endfor %}
          </ul>
            {% if user.is_authenticated %}
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">

              <a href="#" class="dropdown-toggle  pull-right" data-toggle="dropdown">

                更多

               <span class="caret "></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="/bbs_pub/">写博闻</a></li>
                <li><a href="/ziliao/">资料编辑</a></li>


              </ul>

            </li>
          </ul>
            {% endif %}


          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle  pull-right" data-toggle="dropdown">
              {% if user.is_authenticated%}
                {{user.username}}
                
              {%else%} 
                登陆
               {%endif%}
               <span class="caret "></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="/login/">登陆</a></li>
                <li><a href="/logout/">退出</a></li>
                  <li><a href="/zhuce/">注册</a></li>


              </ul>
            </li>
          </ul>

        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container  center-container-hx ">
    {% block page-content %}
      <!-- Main component for a primary marketing message or call to action -->
      <div class="contents">
          {% for bbs in bbs_list reversed %}
            <a href="/detail/{{bbs.id}}/" >{{ bbs.title}}</a><h6>{{ bbs.created_at }}</h6>
            <br>
            {{bbs.summary}}
            <hr>
          {%endfor%}
      </div>
    {% endblock %}
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/js/jquery-2.1.1.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
   
  

</body></html>