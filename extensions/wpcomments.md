---
layout: extension
name: wpcomments
title: WordPress Comments for CKAN Datasets
author: Helsinki Region Infoshare
homepage: https://github.com/Helsingin-kaupungin-tietokeskus/ckanext-comments
github_user: Helsingin-kaupungin-tietokeskus
github_repo: ckanext-comments
category: Extension
featured: 
permalink: /extension/wpcomments/
---


This plugin brings comments from WordPress to CKAN dataset pages.
Includes reporting of comments and subscribing to comments features,
latter of which is deemed specific to Helsinki Region Infoshare.

This plugin requires a relatively new WordPress installation to be
present under the exact same domain name, so Ajax-queries to
.../xmlrpc.php and .../wp-admin/admin-ajax.php will succeed. The plugin
assumes that there is a WordPress post related to each CKAN dataset.
Required changes to WordPress XML-RPC API are provided based on
implementation in
<a href="https://github.com/Helsingin-kaupungin-tietokeskus/wordpress" class="uri">https://github.com/Helsingin-kaupungin-tietokeskus/wordpress</a>

Modification of example Javascript and PHP code is required to make this
plugin work.

Install (CKAN)
==============

In an activated python environment run: pip install -e
git+<a href="https://github.com/Helsingin-kaupungin-tietokeskus/ckanext-comments.git#egg=ckanext-comments" class="uri">https://github.com/Helsingin-kaupungin-tietokeskus/ckanext-comments.git#egg=ckanext-comments</a>

\[The plugin is compatible only with CKAN 2.x versions\]

Tested with: CKAN 2.1.1, WordPress 3.9.1 / WordPress 4.2.2

Enabling (CKAN)
===============

Enable by adding to your ckan.plugins line in CKAN config:

ckan.plugins = ... comments

To your theme plugin, add:

{%raw%}{% {%endraw%}snippet 'snippets/comments.html', package\_name =
pkg\_dict.name, wp\_url = 'www.your.wordpress.installati.on',
comment\_subscribing = False, subscription\_action\_url = '',
wordpress\_user\_id = False{%raw%} %}{%endraw%}

package\_name: Name (slug) of the dataset. wp\_url: URL of your
WordPress installation. comment\_subscribing: True/False for
enabĺing/disabling comment subscription feature. Effectively HRI
specific. subscription\_action\_url: Form target for comment
subscription, related to the setting above. HRI specific.
wordpress\_user\_id: Logged in user's ID from WordPress or False.

This will enable commenting and reporting features. You may provide
wordpress\_user\_id in order to link the comment to the logged in user
on the WordPress side.

The reporting feature requires additional setup. Add this script after
the snippet call:

<script type="text/javascript"> function
setCommentReportingCommentIdAndAction(element) {

    if(HRI_LANG && HRI_LANG === 'en') {

      target = 'http://' + wordpress_url + '/en/report-comment/';
      hri_blog = 2;
    }
    else {

      target = 'http://' + wordpress_url + '/fi/ilmoita-kommentti/';
      hri_blog = 1;
    }

    $('#comment_ID').val( $(element).attr('id').substr(7) + '-' + hri_blog);
    $('#report-form').attr('action', target);

} </script>

Modify the script above to set target and comment id fields to suitable
values. The target page will receive variables: comment\_ID,
report-email and reporttext in POST. For a complete example of report
handling with this input, you may refer to:
<a href="https://github.com/Helsingin-kaupungin-tietokeskus/wordpress/blob/master/wp-content/themes/hri2/page-report.php" class="uri">https://github.com/Helsingin-kaupungin-tietokeskus/wordpress/blob/master/wp-content/themes/hri2/page-report.php</a>

To set up jQuery plugin handling the comments, do:

    <script type="text/javascript">
    window.onload = function() {

    var comments_options = {
      packagename: '{{ pkg.name }}',
      // post_id:     post_id,
      // comments:    $.parseJSON(data),
      xmlrpcurl:   'http://www.your.wordpress.installati.on',
      oncommentsuccess: function() { /* ... */ },
      blog_id:      '0',
      parselocalizeddate: function() { /* Localized date parser - fill this in. see dateFromFinnishDate in the plugin for an example. */ },
      phrases:     {
        no_wp_id_found:    "{{ _('Commenting is unavailable for this dataset.') }}",
        reply:             "{{ _('Reply') }}",
        report:            "{{ _('Report inappropriate content') }}",
        already_said:      "{{ _('Duplicate comment detected; it looks as though you\'ve already said that!') }}",
        subscribe_success: "{{ _('Successfully subscribed to comments on this page.') }}",
        subscribe_rem:     "{{ _('Your subscription to comments on this page was succesfully removed.') }}",
        subscribe_remall:  "{{ _('Succesfully removed all your subscriptions to comments on this site.') }}",
        subscribe_fail:    "{{ _('Already subscribed to post\'s comments.') }}",
        subscribe_remfail: "{{ _('Cannot remove a non-existing subscription.') }}"
      }
    }

    $.comments(comments_options);
    }
    </script>

Note that instead of hardcoding your WordPress installation URL like
'<a href="http://www.your.wordpress.installati.on" class="uri">http://www.your.wordpress.installati.on</a>',
you'll probably want to have a helper like
'<a href="http://" class="uri">http://</a>{{ h.wordpress\_url() }}' to
provide it from the .ini settings file. Settings for $.comments can be
reviewed from the jQuery plugin's code.

List of WordPress API-calls made by the jQuery plugin follows. Note that
these must be implemented in a WordPress theme or plugin, example
implementations are provided in the next chapter.

    url: settings.xmlrpcurl + '/xmlrpc.php',
    methodName: 'wp.getPostId',
    params: [settings.wordpress_username, settings.wordpress_password, settings.packagename]

    Will be called on init if the setting post_id is not provided.

    url: settings.xmlrpcurl + '/xmlrpc.php',
    methodName: 'hri.getComments',
    params: [settings.blog_id, settings.wordpress_username, settings.wordpress_password, {'post_id': settings.post_id}]

    Will be called on init if the comments are not provided.

    url: settings.xmlrpcurl + '/xmlrpc.php',
    methodName: 'hri.newComment',
    params: [settings.blog_id, settings.wordpress_username, settings.wordpress_password, settings.post_id, {'comment_parent': settings.comment_parent, 'content': settings.content, 'author': settings.author, 'author_url': settings.author_url, 'author_email': settings.author_email, 'user_id': settings.user_id}]

    Called when submitting a new comment.

These functions are deemed as HRI specific and as such only mentioned
here.

    url: settings.xmlrpcurl + '/xmlrpc.php',
    methodName: 'hri.subscribeToComments',
    params: [settings.wordpress_username, settings.wordpress_password, settings.post_id, settings.email]

    url: settings.xmlrpcurl + '/xmlrpc.php',
    methodName: 'hri.removeSubscriptionToComments',
    params: [settings.wordpress_username, settings.wordpress_password, settings.post_id, settings.email],

    url: settings.xmlrpcurl + '/xmlrpc.php',
    methodName: 'hri.removeAllSubscriptionsToComments',
    params: [settings.wordpress_username, settings.wordpress_password, settings.email],

Enabling (WordPress)
====================

As mentioned before, the WordPress API must be extended to support
querying a post's id, getting comments for the post and submitting a new
comment for the post. In this chapter we present example implementations
based on
<a href="https://github.com/Helsingin-kaupungin-tietokeskus/wordpress/blob/master/wp-content/plugins/hri-ckan/" class="uri">https://github.com/Helsingin-kaupungin-tietokeskus/wordpress/blob/master/wp-content/plugins/hri-ckan/</a>

In the plugin we introduce extensions to the XML-RPC API by adding the
following lines - note that the jQuery plugin expects the functions to
be with these exact same names:

    add_filter('xmlrpc_methods', 'hri_xmlrpc_methods');
    function hri_xmlrpc_methods($methods) {
      $methods['wp.getPostId'] = 'ckan_find_wordpress_post_id';
      $methods['hri.getComments'] = 'hri_getComments';
      $methods['hri.newComment'] = 'hri_newComment';
      return $methods;
    }

    require( ABSPATH . 'wp-content/plugins/hri-ckan/function_xml_rpc.php' );

Which are then defined in the
<a href="https://github.com/Helsingin-kaupungin-tietokeskus/wordpress/blob/master/wp-content/plugins/hri-ckan/function_xml_rpc.php" class="uri">https://github.com/Helsingin-kaupungin-tietokeskus/wordpress/blob/master/wp-content/plugins/hri-ckan/function_xml_rpc.php</a>
as:

    /**
     * Search a post's WordPress post_id by slug
     * This functionality is required when transferring posts' comments
     * over to CKAN.
     *
     * @param mixed $args
     * @return int $post_id
     * @author Janne Mikkonen <janne.mikkonen@hiq.fi>
     */
    function ckan_find_wordpress_post_id($args) {
        
        ini_set('html_errors', 0);
        // Parse the arguments, assuming they're in the correct order
        $username   = $args[0];
        $password   = $args[1];
        $slug       = $args[2];
        
        global $wp_xmlrpc_server;
        
        // Let's run a check to see if credentials are okay
        /* if(!$user = $wp_xmlrpc_server->login($username, $password)) {
            return $wp_xmlrpc_server->error;
        } */
        global $wpdb;
        
        return $wpdb->get_results( "SELECT DISTINCT p.ID FROM {$wpdb->posts} p JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id WHERE p.post_type = 'data' AND pm.meta_key = 'ckan_url' AND p.guid LIKE 'http://www.hri.fi/blog/data/{$slug}/' OR p.post_name = '{$slug}' OR pm.meta_value LIKE '%/dataset/{$slug}';" );
    }

The get\_results query above needs to be at least checked, so that it is
able to find the post in your system.

------------------------------------------------------------------------

    function hri_convert_date( $date ) {
        if ( $date === '0000-00-00 00:00:00' ) {
            return new IXR_Date( '00000000T00:00:00Z' );
        }
        return mysql2date( 'd.m.Y H:i', $date, false );
    }
    function hri_convert_date_gmt( $date_gmt, $date ) {
        if ( $date !== '0000-00-00 00:00:00' && $date_gmt === '0000-00-00 00:00:00' ) {
            return new IXR_Date( get_gmt_from_date( mysql2date( 'Y-m-d H:i:s', $date, false ), 'Ymd\TH:i:s' ) );
        }
        return hri_convert_date( $date_gmt );
    }

    function hri_prepare_comment( $comment ) {
        // Format page date.
        $comment_date = hri_convert_date( $comment->comment_date );
        $comment_date_gmt = hri_convert_date_gmt( $comment->comment_date_gmt, $comment->comment_date );
        if ( '0' == $comment->comment_approved )
            $comment_status = 'hold';
        else if ( 'spam' == $comment->comment_approved )
            $comment_status = 'spam';
        else if ( '1' == $comment->comment_approved )
            $comment_status = 'approve';
        else
            $comment_status = $comment->comment_approved;
        $_comment = array(
            'date_created_gmt' => $comment_date_gmt,
            'user_id'          => $comment->user_id,
            'comment_id'       => $comment->comment_ID,
            'parent'           => $comment->comment_parent,
            'status'           => $comment_status,
            'content'          => $comment->comment_content,
            // 'link'             => get_comment_link($comment),
            'post_id'          => $comment->comment_post_ID,
            // 'post_title'       => get_the_title($comment->comment_post_ID),
            'author'           => $comment->comment_author,
            'author_url'       => $comment->comment_author_url,
            // 'author_email'     => $comment->comment_author_email, // Let's Not return this for anyone (with Firebug etc.) to see.
            // 'author_ip'        => $comment->comment_author_IP,
            'type'             => $comment->comment_type,
        );
        if ( $comment->user_id > 0 && $user = get_userdata($comment->user_id) ) {
            $_comment['avatar_src'] = $user->avatar;
        }
        return apply_filters( 'xmlrpc_prepare_comment', $_comment, $comment );
    }

    /**
     * NOTE! This is modified wp_xmlrpc_server::wp_getComments from wp-includes/class-wp-xmlrpc-server.php
     *
     * Removed $this->login($username, $password) and current_user_can( 'moderate_comments' ) requirement.
     *
     * @param array $args Method parameters.
     * @return array. Contains a collection of comments. See {@link wp_xmlrpc_server::wp_getComment()} for a description of each item contents
     */
    function hri_getComments($args) {
        hri_escape($args);
        $blog_id    = (int) $args[0];
        $username   = $args[1];
        $password   = $args[2];
        $struct     = isset( $args[3] ) ? $args[3] : array();
        do_action('xmlrpc_call', 'wp.getComments');
        if ( isset($struct['status']) )
            $status = $struct['status'];
        else
            $status = '';
        $post_id = '';
        if ( isset($struct['post_id']) )
            $post_id = absint($struct['post_id']);
        $offset = 0;
        if ( isset($struct['offset']) )
            $offset = absint($struct['offset']);
        $number = 25;
        if ( isset($struct['number']) )
            $number = absint($struct['number']);
        $comments = get_comments( array('status' => $status, 'post_id' => $post_id, 'offset' => $offset, 'number' => $number ) );
        $comments_struct = array();
        foreach ( $comments as $comment ) {
            $comments_struct[] = hri_prepare_comment( $comment );
        }
        return $comments_struct;
    }

These functions should work fine as-is.

------------------------------------------------------------------------

    function hri_escape(&$array) {
        global $wpdb;
        if (!is_array($array)) {
            return($wpdb->escape($array));
        } else {
            foreach ( (array) $array as $k => $v ) {
                if ( is_array($v) ) {
                    hri_escape($array[$k]);
                } else if ( is_object($v) ) {
                    //skip
                } else {
                    $array[$k] = $wpdb->escape($v);
                }
            }
        }
    }

    /**
     * NOTE! This is modified wp_xmlrpc_server::wp_newComment from wp-includes/class-wp-xmlrpc-server.php
     *
     * Removed $this->login($username, $password) and login requirement.
     *
     * @param array $args Method parameters.
     * @return mixed {@link wp_new_comment()}
     */
    function hri_newComment($args) {
        
        global $wpdb;
        hri_escape($args);
        $blog_id        = (int) $args[0];
        $username       = $args[1];
        $password       = $args[2];
        $post           = $args[3];
        $content_struct = $args[4];
        $user_id        = (int) $content_struct['user_id'];
        if ( is_numeric($post) )
            $post_id = absint($post);
        else
            $post_id = url_to_postid($post);
        if ( ! $post_id )
            return new IXR_Error( 404, __( 'Invalid post ID.' ) );
        if ( ! get_post($post_id) )
            return new IXR_Error( 404, __( 'Invalid post ID.' ) );
        $comment['comment_post_ID'] = $post_id;
        if ($user_id && $user = get_userdata($user_id)) {
            $comment['comment_author'] = $wpdb->escape( $user->display_name );
            $comment['comment_author_email'] = $wpdb->escape( $user->user_email );
            $comment['comment_author_url'] = $wpdb->escape( $user->user_url );
            $comment['user_ID'] = $user->ID;
        } else {
            $comment['comment_author'] = '';
            if ( isset($content_struct['author']) )
                $comment['comment_author'] = $content_struct['author'];
            $comment['comment_author_email'] = '';
            if ( isset($content_struct['author_email']) )
                $comment['comment_author_email'] = $content_struct['author_email'];
            $comment['comment_author_url'] = '';
            if ( isset($content_struct['author_url']) )
                $comment['comment_author_url'] = $content_struct['author_url'];
            $comment['user_ID'] = 0;
            if ( 6 > strlen($comment['comment_author_email']) || '' == $comment['comment_author'] )
                return new IXR_Error( 403, __( 'Comment author name and email are required' ) );
            elseif ( !is_email($comment['comment_author_email']) )
                return new IXR_Error( 403, __( 'A valid email address is required' ) );
        }
        $comment['comment_parent']  = isset($content_struct['comment_parent']) ? absint($content_struct['comment_parent']) : 0;
        $comment['comment_content'] = isset($content_struct['content']) ? $content_struct['content'] : null;
        do_action('xmlrpc_call', 'wp.newComment');
        $comment_ID = wp_new_comment( $comment );
        do_action( 'xmlrpc_call_success_wp_newComment', $comment_ID, $args );
        return $comment_ID;
    }

These functions should work fine as-is as well.

------------------------------------------------------------------------

