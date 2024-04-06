# `rich-click` CLI tool

## Overview

**rich-click** comes with a CLI tool that allows you to format the Click help output for any CLI that uses Click.

<div class="termy">
```console
$ rich-click --help

 <span style="color: #808000; text-decoration-color: #808000">Usage:                                                       </span>          
 <span style="font-weight: bold">rich_click                                                   </span>          
 [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">OPTIONS</span>] [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">SCRIPT</span> | <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">MODULE</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">CLICK_COMMAND</span>] [-- <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">SCRIPT_ARGS</span>...]          
                                                                        
 The <a href="https://github.com/ewels/rich-click">rich-click</a> CLI provides attractive help output from any tool using 
 <a href="https://click.palletsprojects.com/">click</a>, formatted with <a href="https://github.com/Textualize/rich">rich</a>.                                            

// The rest of the output is omitted
```
</div>

To use, simply prefix `rich-click` to the command. Here are a few examples:

=== "<code>flask</code>"

    <div class="termy">
    ```console
    $ rich-click flask --help

     <span style="color: #808000; text-decoration-color: #808000">Usage:</span> <span style="font-weight: bold">flask</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">OPTIONS</span>] <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">COMMAND</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">ARGS</span>]...

     A general utility script for Flask applications.
     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">An application to load must be given with the &#x27;</span><span style="color: #7fbfbf; text-decoration-color: #7fbfbf; font-weight: bold">--app</span><span style="color: #7f7f7f; text-decoration-color: #7f7f7f">&#x27; option, </span>
     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">&#x27;FLASK_APP&#x27; environment variable, or with a &#x27;wsgi.py&#x27; or &#x27;app.py&#x27; file</span>
     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">in the current directory.</span>

    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Options ────────────────────────────────────────────────────────────╮</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--env-file</span>          <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-e</span>  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">FILE  </span>  Load environment variables from this <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 file. python-dotenv must be          <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 installed.                           <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--app</span>               <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-A</span>  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">IMPORT</span>  The Flask application or factory     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 function to load, in the form        <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 &#x27;module:name&#x27;. Module can be a       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 dotted import or file path. Name is  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 not required if it is &#x27;app&#x27;,         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 &#x27;application&#x27;, &#x27;create_app&#x27;, or      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 &#x27;make_app&#x27;, and can be &#x27;name(args)&#x27;  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                 to pass arguments.                   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--debug</span>/<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--no-debug</span>      <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">      </span>  Set debug mode.                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--version</span>               <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">      </span>  Show the Flask version.              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--help</span>                  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">      </span>  Show this message and exit.          <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰──────────────────────────────────────────────────────────────────────╯</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Commands ───────────────────────────────────────────────────────────╮</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">routes       </span> Show the routes for the app.                           <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">run          </span> Run a development server.                              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">shell        </span> Run a shell in the app context.                        <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰──────────────────────────────────────────────────────────────────────╯</span>
    ```
    </div>

=== "<code>celery</code>"

    <div class="termy">
    ```console
    $ rich-click celery --help

     <span style="color: #808000; text-decoration-color: #808000">Usage:</span> <span style="font-weight: bold">celery</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">OPTIONS</span>] <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">COMMAND</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">ARGS</span>]...

     Celery command entrypoint.

    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Options ──────────────────────────────────────────────────────────────╮</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--app</span>             <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-A</span>  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">APPLICATION</span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--broker</span>          <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-b</span>  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT       </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--result-backend</span>      <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT       </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--loader</span>              <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT       </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--config</span>              <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT       </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--workdir</span>             <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">PATH       </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--no-color</span>        <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-C</span>  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">           </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--quiet</span>           <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-q</span>  <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">           </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--version</span>             <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">           </span>                                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--skip-checks</span>         <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">           </span>  Skip Django core checks on startup. <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                    Setting the SKIP_CHECKS environment <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                    variable to any non-empty string    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                    will have the same effect.          <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--help</span>                <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">           </span>  Show this message and exit.         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰────────────────────────────────────────────────────────────────────────╯</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Commands ─────────────────────────────────────────────────────────────╮</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">amqp    </span> AMQP Administration Shell.                                    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">beat    </span> Start the beat periodic task scheduler.                       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">call    </span> Call a task by name.                                          <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">control </span> Workers remote control.                                       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">events  </span> Event-stream utilities.                                       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">graph   </span> The ``celery graph`` command.                                 <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">inspect </span> Inspect the worker at runtime.                                <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">list    </span> Get info from broker.                                         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">logtool </span> The ``celery logtool`` command.                               <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">migrate </span> Migrate tasks from one broker to another.                     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">multi   </span> Start multiple worker instances.                              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">purge   </span> Erase all messages from all known task queues.                <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">report  </span> Shows information useful to include in bug-reports.           <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">result  </span> Print the return value for a given task id.                   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">shell   </span> Start shell session with convenient access to celery symbols. <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">status  </span> Show list of workers that are online.                         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">upgrade </span> Perform upgrade between versions.                             <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">worker  </span> Start worker instance.                                        <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰────────────────────────────────────────────────────────────────────────╯</span>


     Specify one of these sub-commands and you can find more help from there.
    ```
    </div>

=== "<code>dagster</code>"

    <div class="termy">
    ```console
    $ rich-click dagster --help
     <span style="color: #808000; text-decoration-color: #808000">Usage:</span> <span style="font-weight: bold">dagster</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">OPTIONS</span>] <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">COMMAND</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">ARGS</span>]...

     CLI tools for working with Dagster.

    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Options ──────────────────────────────────────────────────────────────╮</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--version</span>  <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-v</span>    Show the version and exit.                            <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--help</span>     <span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-h</span>    Show this message and exit.                           <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰────────────────────────────────────────────────────────────────────────╯</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Commands ─────────────────────────────────────────────────────────────╮</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">asset       </span> Commands for working with Dagster assets.                 <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">code-server </span> Commands for working with Dagster code servers.           <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">debug       </span> Commands for helping debug Dagster issues by dumping or   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">            </span> loading artifacts from specific runs.                     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">dev         </span> Start a local deployment of Dagster, including            <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">            </span> dagster-webserver running on localhost and the            <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">            </span> dagster-daemon running in the background                  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">instance    </span> Commands for working with the current Dagster instance.   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">job         </span> Commands for working with Dagster jobs.                   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">project     </span> Commands for bootstrapping new Dagster projects and code  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">            </span> locations.                                                <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">run         </span> Commands for working with Dagster job runs.               <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">schedule    </span> Commands for working with Dagster schedules.              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">sensor      </span> Commands for working with Dagster sensors.                <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰────────────────────────────────────────────────────────────────────────╯</span>
    ```
    </div>

If the CLI is not installed as a script, you can also pass the location with: `<module_name>:<click_command_name>`.

For example, if you have a file located at `path/to/my/cli.py`, and the Click `Command` object is named `main`, then you can run: `rich-click path.to.my.cli:main`.

## Render help text as HTML or SVG

You can also use `rich-click --output=html [command]` to render rich HTML for help text, or `rich-click --output=svg [command]` to generate an SVG.

This works for RichCommands as well as normal click Commands.

Notably, we used this functionality to help write these docs you are reading right now. :)

<div class="termy" static>
```console
$ rich-click --output=html flask --help

&lt;span style=&quot;color: #808000; text-decoration-color: #808000&quot;&gt;Usage:&lt;/span&gt; &lt;span style=&quot;font-weight: bold&quot;&gt;flask&lt;/span&gt; [&lt;span style=&quot;color: #008080; text-decoration-color: #008080; font-weight: bold&quot;&gt;OPTIONS&lt;/span&gt;] &lt;span style=&quot;color: #008080; text-decoration-color: #008080; font-weight: bold&quot;&gt;COMMAND&lt;/span&gt; [&lt;span style=&quot;color: #008080; text-decoration-color: #008080; font-weight: bold&quot;&gt;ARGS&lt;/span&gt;]...

A general utility script for Flask applications.  
 &lt;span style=&quot;color: #7f7f7f; text-decoration-color: #7f7f7f&quot;&gt;An application to load must be given with the &amp;#x27;&lt;/span&gt;&lt;span style=&quot;color: #7fbfbf; text-decoration-color: #7fbfbf; font-weight: bold&quot;&gt;--app&lt;/span&gt;&lt;span style=&quot;color: #7f7f7f; text-decoration-color: #7f7f7f&quot;&gt;&amp;#x27; option, &lt;/span&gt;  
 &lt;span style=&quot;color: #7f7f7f; text-decoration-color: #7f7f7f&quot;&gt;&amp;#x27;FLASK_APP&amp;#x27; environment variable, or with a &amp;#x27;wsgi.py&amp;#x27; or &amp;#x27;app.py&amp;#x27; file&lt;/span&gt;
&lt;span style=&quot;color: #7f7f7f; text-decoration-color: #7f7f7f&quot;&gt;in the current directory.&lt;/span&gt;

// The rest of the output is omitted

```
</div>

## Notes on how the `rich-click` CLI works

Under the hood, the `rich-click` CLI is patching the `click` module, and replacing the Click decorators and `click.Command`, `click.Group`, etc. objects with their equivalent **rich-click** versions.

Sometimes, a subclassed `click.Command` will overwrite one of these methods:

- `click.Command.format_usage`
- `click.Command.format_help_text`
- `click.Command.format_options`
- `click.MultiCommand.format_commands`
- `click.Command.format_epilog`

Patching Click internals can mess with method resolution order,
since by the time the downstream library subclasses the `click.Command`, it will be a `RichCommand`, and the subclass's method will take precedence over the `RichCommand`'s methods.
The problem is that **rich-click**'s methods can be incompatible or at least stylistically incongruous with the base Click help text rendering.

To solve this, `rich-click` checks whether a method comes from a "true" `RichCommand` subclass or if it just looks that way due to patching.
If `RichCommand` is "properly" subclassed, the override is allowed.
If the subclass is only a result of the patching operation, we ignore the aforementioned methods and use the **rich-click** implementation.

Long story short, the `rich-click` CLI is safe to subclassing when it is the user's intent to subclass a **rich-click** object. (This is so that you can use other nifty features of the CLI such as the `--output` option on your own **rich-click** CLIs)
That said, custom, non-**rich-click** implementations are ignored.

### Using `patch()` as an end user

The functionality that `rich-click` uses to patch Click internals is available for use by **rich-click** end users,
and it occasionally comes in handy outside of the `rich-click` CLI.

In some situations, you might be registering a command from another Click CLI that does not use Rich-Click:

```python
import rich_click as click
from some_library import another_cli

@click.group("my-cli")
def cli():
    pass

# `another_cli` will NOT have rich-click markup. :(
cli.add_command(another_cli)
```

In this situation, `another_cli` retains its original help text behavior.
In order to make `another_cli` work with Rich-Click, you need to patch `click` before you import `another_cli`.
You can patch Click with `rich_click.patch.patch` like this:

```python
import rich_click as click
from rich_click.patch import patch

patch()

from some_library import another_cli  # noqa: E402

@click.group("my-cli")
def cli():
    pass

# `another_cli` will have rich-click markup. :)
cli.add_command(another_cli)
```
