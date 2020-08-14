import 'package:flutter/material.dart';
import './text_output.dart';

class TextControl extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _TextControlState();
  }
}
class _TextControlState extends State<TextControl> {
  var _mainText = 'This is the first assignment';

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextOutput(_mainText),
        RaisedButton(
          child: Text('Change text!'),
          color: Colors.blue,
          textColor: Colors.white,
          onPressed: () {
          setState(() {
            _mainText = 'This changed!';
          });

        })
      ],      
    );
  }
}