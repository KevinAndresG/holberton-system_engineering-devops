<p>Using <code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using t (instead of using Bash as you were previously doing).</p>

<p>Hint:</p>

<ul>
<li><code>strace</code> can attach to a current running process</li>
<li>You can use <a href="/rltoken/4KkxME6-3aY9fgfok6HNFA" title="tmux" target="_blank">tmux</a> to run <a href="/rltoken/OUc10nTtuZG65adFVbkYag" title="strace" target="_blank">strace</a> in one window and <code>curl</code> in another one</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Your <code>0-strace_is_your_friend.pp</code> file must contain t code</li>
<li>You can use whatever t resource type you want for you fix</li>
</ul>
